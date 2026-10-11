from django.contrib import admin
from django.utils.html import format_html

from .models import JobApplication, JobOpening


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "location", "job_type", "is_open", "display_order", "application_count")
    list_editable = ("is_open", "display_order")
    list_filter = ("is_open", "department", "job_type")
    search_fields = ("title", "department")
    prepopulated_fields = {"slug": ("title",)}

    @admin.display(description="Applications")
    def application_count(self, obj):
        return obj.applications.count()


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("reference", "full_name", "job_title", "email", "phone", "experience_years", "status", "applied_at")
    list_filter = ("status", "job", "applied_at")
    list_editable = ("status",)
    search_fields = ("full_name", "email", "phone", "job_title", "current_company")
    date_hierarchy = "applied_at"
    readonly_fields = ("reference", "job", "job_title", "applied_at", "updated_at", "resume_link")
    fieldsets = (
        ("Application", {"fields": ("reference", "job", "job_title", "status", "applied_at", "updated_at")}),
        ("Applicant", {"fields": ("full_name", "email", "phone", "current_location", "current_company")}),
        ("Profile", {"fields": ("experience_years", "notice_period", "expected_salary", "linkedin_url", "portfolio_url")}),
        ("Answers", {"fields": ("screening_answer", "cover_letter")}),
        ("Resume", {"fields": ("resume", "resume_link")}),
        ("Internal", {"fields": ("internal_notes",)}),
    )

    @admin.display(description="Open resume")
    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank" rel="noopener">Download / view</a>', obj.resume.url)
        return "—"
