import os
import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify

from .validators import validate_resume_size


class JobOpening(models.Model):
    """A role shown on the Careers page. Manage these from Django admin."""

    JOB_TYPES = [
        ("full-time", "Full-time"),
        ("part-time", "Part-time"),
        ("contract", "Contract"),
        ("internship", "Internship"),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    department = models.CharField(max_length=80)
    location = models.CharField(max_length=120, help_text="e.g. Remote (India) or Kolkata (Hybrid)")
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default="full-time")
    summary = models.TextField(help_text="Short paragraph shown at the top of the application form.")
    responsibilities = models.TextField(blank=True, help_text="One item per line.")
    requirements = models.TextField(blank=True, help_text="One item per line.")
    screening_question = models.CharField(
        max_length=255, blank=True,
        help_text="Optional job-specific question the applicant must answer (e.g. 'Link to your GitHub or portfolio').",
    )
    is_open = models.BooleanField(default=True, help_text="Untick to hide this role and stop accepting applications.")
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "job"
            slug, n = base, 2
            while JobOpening.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def meta_line(self):
        return f"{self.department} · {self.location} · {self.get_job_type_display()}"

    def responsibilities_list(self):
        return [l.strip() for l in self.responsibilities.splitlines() if l.strip()]

    def requirements_list(self):
        return [l.strip() for l in self.requirements.splitlines() if l.strip()]


def resume_upload_path(instance, filename):
    # Random name so resumes can't be guessed/enumerated from the URL.
    ext = os.path.splitext(filename)[1].lower()
    return f"resumes/{instance.job_id}/{uuid.uuid4().hex}{ext}"


class JobApplication(models.Model):
    """One submitted application. Stored in the company database."""

    STATUS_CHOICES = [
        ("new", "New"),
        ("reviewing", "Under review"),
        ("shortlisted", "Shortlisted"),
        ("interview", "Interview scheduled"),
        ("rejected", "Rejected"),
        ("hired", "Hired"),
    ]

    job = models.ForeignKey(JobOpening, on_delete=models.PROTECT, related_name="applications")
    # Copy of the title at time of applying, so history survives if the job is renamed.
    job_title = models.CharField(max_length=150, editable=False)

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    current_location = models.CharField(max_length=120)
    current_company = models.CharField(max_length=150, blank=True)
    experience_years = models.DecimalField(max_digits=4, decimal_places=1, help_text="Total years of experience")
    notice_period = models.CharField(max_length=60, blank=True, help_text="e.g. Immediate, 30 days")
    expected_salary = models.CharField(max_length=60, blank=True, help_text="Expected annual salary (optional)")
    linkedin_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    screening_answer = models.TextField(blank=True)
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(
        upload_to=resume_upload_path,
        validators=[FileExtensionValidator(["pdf", "doc", "docx"]), validate_resume_size],
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    internal_notes = models.TextField(blank=True, help_text="Visible to staff only.")
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-applied_at"]
        constraints = [
            models.UniqueConstraint(fields=["job", "email"], name="one_application_per_email_per_job"),
        ]

    def __str__(self):
        return f"{self.full_name} → {self.job_title}"

    @property
    def reference(self):
        return f"INK-APP-{self.pk:05d}"

    def save(self, *args, **kwargs):
        if not self.job_title:
            self.job_title = self.job.title
        self.email = self.email.strip().lower()
        super().save(*args, **kwargs)
