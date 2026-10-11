from django.db import migrations

JOBS = [
    {
        "title": "Frontend Engineer", "slug": "frontend-engineer", "department": "Engineering",
        "location": "Remote (India)", "job_type": "full-time", "display_order": 1,
        "summary": "Help us build a fast, beautiful storefront for readers across India. You'll own features end to end — from design handoff to production.",
        "responsibilities": "Build and maintain responsive storefront pages\nTurn designs into accessible, pixel-accurate UI\nImprove page speed and Core Web Vitals\nWork with backend engineers on Django templates and APIs",
        "requirements": "2+ years of HTML, CSS and JavaScript\nComfort with responsive layouts and accessibility\nFamiliarity with Django templates or a similar stack is a plus\nA portfolio or GitHub we can look at",
        "screening_question": "Link to a project, portfolio or GitHub profile you're proud of, and tell us why.",
    },
    {
        "title": "Catalog & Curation Associate", "slug": "catalog-curation-associate", "department": "Operations",
        "location": "Kolkata (Hybrid)", "job_type": "full-time", "display_order": 2,
        "summary": "Keep our catalogue accurate and interesting. You'll add titles, maintain metadata and help curate collections our readers love.",
        "responsibilities": "Add and update book listings, prices and stock\nWrite short, engaging descriptions and collections\nKeep author, ISBN and category data clean\nSpot gaps in the catalogue and suggest new titles",
        "requirements": "Love of books across genres\nStrong attention to detail\nGood written English (Bengali/Hindi a plus)\nComfortable with spreadsheets",
        "screening_question": "Tell us about a book you'd recommend to a first-time reader and why.",
    },
    {
        "title": "Customer Support Specialist", "slug": "customer-support-specialist", "department": "Support",
        "location": "Remote (India)", "job_type": "full-time", "display_order": 3,
        "summary": "Be the friendly voice of Inkwell. You'll help readers with orders, returns and recommendations over email and chat.",
        "responsibilities": "Respond to customer queries by email and chat\nTrack orders and resolve delivery issues\nHandle returns and refunds politely and quickly\nShare feedback with the team to improve the store",
        "requirements": "Excellent written and spoken communication\nPatience and a customer-first attitude\nPrior support experience preferred\nWillingness to work flexible shifts",
        "screening_question": "A customer's order is a week late and they're upset. How would you reply?",
    },
    {
        "title": "Warehouse & Fulfilment Associate", "slug": "warehouse-fulfilment-associate", "department": "Logistics",
        "location": "Kolkata (On-site)", "job_type": "full-time", "display_order": 4,
        "summary": "Make sure every order leaves our Salt Lake warehouse packed with care and on time.",
        "responsibilities": "Pick, pack and dispatch orders accurately\nInspect books and handle returns\nKeep shelves organised and stock counts correct\nFollow safety and packing standards",
        "requirements": "Reliable and detail-oriented\nAble to lift and move boxes\nBasic smartphone/computer skills\nPrior warehouse experience is a plus",
        "screening_question": "",
    },
]


def seed(apps, schema_editor):
    JobOpening = apps.get_model("careers", "JobOpening")
    for j in JOBS:
        JobOpening.objects.get_or_create(slug=j["slug"], defaults=j)


def unseed(apps, schema_editor):
    apps.get_model("careers", "JobOpening").objects.filter(slug__in=[j["slug"] for j in JOBS]).delete()


class Migration(migrations.Migration):
    dependencies = [("careers", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
