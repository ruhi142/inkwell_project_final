import re

from django import forms

from .models import JobApplication


class ApplicationForm(forms.ModelForm):
    # Honeypot: real users never see or fill this; bots usually do.
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))

    class Meta:
        model = JobApplication
        fields = [
            "full_name", "email", "phone", "current_location", "current_company",
            "experience_years", "notice_period", "expected_salary",
            "linkedin_url", "portfolio_url", "screening_answer", "cover_letter", "resume",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "98765 43210", "inputmode": "tel"}),
            "current_location": forms.TextInput(attrs={"placeholder": "City, State"}),
            "current_company": forms.TextInput(attrs={"placeholder": "Where you work now (if any)"}),
            "experience_years": forms.NumberInput(attrs={"placeholder": "e.g. 2.5", "step": "0.5", "min": "0", "max": "60"}),
            "notice_period": forms.TextInput(attrs={"placeholder": "e.g. Immediate, 30 days"}),
            "expected_salary": forms.TextInput(attrs={"placeholder": "e.g. ₹6 LPA"}),
            "linkedin_url": forms.URLInput(attrs={"placeholder": "https://linkedin.com/in/…"}),
            "portfolio_url": forms.URLInput(attrs={"placeholder": "https://…"}),
            "screening_answer": forms.Textarea(attrs={"rows": 3}),
            "cover_letter": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us why you'd be a great fit…"}),
            "resume": forms.ClearableFileInput(attrs={"accept": ".pdf,.doc,.docx"}),
        }
        labels = {
            "experience_years": "Total experience (years)",
            "current_company": "Current company",
            "linkedin_url": "LinkedIn profile",
            "portfolio_url": "Portfolio / GitHub",
            "resume": "Resume (PDF, DOC or DOCX, max 5 MB)",
        }

    def __init__(self, *args, job=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        for name in ("current_company", "notice_period", "expected_salary", "linkedin_url", "portfolio_url", "cover_letter"):
            self.fields[name].required = False

        # Job-specific question (set per opening in admin)
        if job and job.screening_question:
            self.fields["screening_answer"].label = job.screening_question
            self.fields["screening_answer"].required = True
        else:
            del self.fields["screening_answer"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        digits = re.sub(r"\D", "", phone)
        if digits.startswith("91") and len(digits) == 12:
            digits = digits[2:]
        if len(digits) < 10 or len(digits) > 13:
            raise forms.ValidationError("Enter a valid phone number.")
        return phone

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if self.job and JobApplication.objects.filter(job=self.job, email__iexact=email).exists():
            raise forms.ValidationError("You've already applied for this role with this email.")
        return email

    def clean_experience_years(self):
        v = self.cleaned_data["experience_years"]
        if v < 0 or v > 60:
            raise forms.ValidationError("Enter a value between 0 and 60.")
        return v

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("website"):  # honeypot tripped
            raise forms.ValidationError("Submission rejected.")
        return cleaned
