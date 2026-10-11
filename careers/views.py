from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ApplicationForm
from .models import JobApplication, JobOpening


def careers(request):
    jobs = JobOpening.objects.filter(is_open=True)
    return render(request, "careers/careers.html", {"jobs": jobs})


def apply(request, slug):
    job = get_object_or_404(JobOpening, slug=slug, is_open=True)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES, job=job)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.job_title = job.title
            try:
                application.save()
            except IntegrityError:
                form.add_error("email", "You've already applied for this role with this email.")
            else:
                _send_confirmation(application)
                request.session["last_application_id"] = application.pk
                return redirect("careers:apply_success", slug=job.slug)
        else:
            messages.error(request, "Please fix the highlighted fields and try again.")
    else:
        initial = {}
        if request.user.is_authenticated:
            initial["full_name"] = request.user.get_full_name() or request.user.username
            initial["email"] = request.user.email
        form = ApplicationForm(job=job, initial=initial)

    return render(request, "careers/apply.html", {"job": job, "form": form})


def apply_success(request, slug):
    job = get_object_or_404(JobOpening, slug=slug)
    app_id = request.session.get("last_application_id")
    application = JobApplication.objects.filter(pk=app_id, job=job).first() if app_id else None
    if not application:
        return redirect("careers:apply", slug=job.slug)
    return render(request, "careers/apply_success.html", {"job": job, "application": application})


def _send_confirmation(application):
    """Email the applicant a receipt. Never lets a mail hiccup break the submit."""
    try:
        send_mail(
            subject=f"We received your application — {application.job_title}",
            message=(
                f"Hi {application.full_name},\n\n"
                f"Thanks for applying for the {application.job_title} role at Inkwell Books. "
                f"Your reference number is {application.reference}.\n\n"
                "Our team will review your application and get back to you by email if "
                "your profile matches what we're looking for.\n\n"
                "Warm regards,\nTeam Inkwell Books"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[application.email],
            fail_silently=True,
        )
    except Exception:
        pass
