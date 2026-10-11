import re
from datetime import timedelta

from django.shortcuts import render
from django.templatetags.static import static
from django.utils import timezone

from core.views import BEST_SELLERS


# Categories, subcategories and books now live in catalog/catalog_data.py
# (edit that file to manage the shop). catalog/registry.py builds them.
from .registry import CATEGORIES, PARENT_OF

# Vibe/theme tag chips shown on the book detail page — mirrors the little
# descriptive pill row Crossword shows under a book's title (e.g. "Quirky
# Character Dynamics", "Emotional Comedy"). No such data model yet, so a
# small curated set per category/slug stands in for it.
_TAG_PRESETS = {
    "fiction": ["Character-Driven", "Emotional Depth", "Page-Turner", "Book Club Pick"],
    "non-fiction": ["Real-World Insight", "Practical Ideas", "Thought-Provoking"],
    "academic": ["Exam-Ready", "Concept Clarity", "Solved Examples"],
    "children": ["Read-Aloud Favorite", "Gentle Life Lessons", "Colourful Illustrations"],
    "sale": ["Reader Favorite", "Limited Stock", "Great Value"],
    "business-economics": ["Actionable Ideas", "Career Booster", "Real-World Case Studies"],
    "young-adult": ["Coming-of-Age", "Binge-Worthy", "Big Feelings"],
    "bestsellers": ["Reader Favorite", "Widely Recommended", "Editor's Pick"],
}

_PUBLISHERS = ["Inkwell Editions", "Harper Collins India", "Penguin Random House", "Rupa Publications", "Westland Books"]

# Sample reviewer names + comment templates used to seed each book's review
# list with a few realistic-looking reviews. No review model yet, so these
# are picked deterministically per book (same _stable_hash trick as
# rating/reviews/pages) rather than being random on every request.
_SAMPLE_REVIEWERS = [
    "Ananya S.", "Rohan K.", "Priya M.", "Karthik R.", "Fatima A.",
    "Vikram J.", "Sneha P.", "Arjun T.", "Meera N.", "Ishaan D.",
]
_SAMPLE_REVIEW_TEMPLATES = [
    "Couldn't put this one down — {tag} from start to finish. Highly recommend picking up a copy.",
    "The {condition_lower} copy I received was in great shape. The story itself is {tag} and well worth the read.",
    "Bought this on a whim and ended up loving it. Very {tag}, exactly what I was looking for.",
    "A solid read overall. A few slow chapters, but the {tag} moments more than make up for it.",
    "Exactly as described — {condition_lower} condition and delivered quickly. The book itself lives up to the hype.",
    "One of the better {category_lower} titles I've picked up this year. {tag_cap} and easy to recommend.",
]


def _sample_reviews(book_id, tags, condition, category_title, count=3):
    h = _stable_hash(book_id)
    tag = (tags[0] if tags else "engaging").lower()
    reviews = []
    for i in range(count):
        seed = (h * (i + 7)) % 100000
        name = _SAMPLE_REVIEWERS[seed % len(_SAMPLE_REVIEWERS)]
        template = _SAMPLE_REVIEW_TEMPLATES[(seed // 7) % len(_SAMPLE_REVIEW_TEMPLATES)]
        stars = 4 + ((seed // 3) % 2)  # 4 or 5 stars
        days_ago = 3 + (seed % 90)
        text = template.format(
            tag=tag, tag_cap=tag.capitalize(),
            condition_lower=condition.lower(), category_lower=category_title.lower(),
        )
        reviews.append({
            "name": name,
            "initial": name[0],
            "stars": range(stars),
            "date": (timezone.now() - timedelta(days=days_ago)).strftime("%d %b %Y"),
            "text": text,
        })
    return reviews


def _stable_hash(text):
    """Small deterministic hash so a book's rating/reviews/pages stay the
    same across requests without needing a real database column for them."""
    total = 0
    for ch in text:
        total = (total * 31 + ord(ch)) % 100000
    return total


def _bare_or_full_img(img, size=600):
    """Book image fields come in two shapes: a bare Unsplash photo id
    (catalog books) or a full, ready-to-use image URL (home page's
    BEST_SELLERS list). Normalise both into a usable <img src>."""
    if img.startswith(("http://", "https://", "/")):
        return img
    if re.search(r"\.(jpe?g|png|webp|gif|svg|avif)$", img, re.I):
        # your own file: "cover.jpg" lives in catalog/static/catalog/img/books/,
        # or give a path like "core/img/cover.jpg" for any other static folder.
        return static(img if "/" in img else f"catalog/img/books/{img}")
    return f"https://images.unsplash.com/photo-{img}?w={size}&q=80"


def _normalize_book(book, category_slug, category_title):
    book_id = book["id"]
    h = _stable_hash(book_id)
    rating = round(4.0 + (h % 10) / 10, 1)
    reviews = 3 + (h % 240)
    pages = 180 + (h % 340)
    condition = book.get("condition", "New")
    discount = book.get("discount")
    if discount is None and book.get("old_price"):
        discount = round(100 * (book["old_price"] - book["price"]) / book["old_price"])
    savings = max(book.get("old_price", book["price"]) - book["price"], 0)
    tags = (_TAG_PRESETS.get(category_slug)
            or _TAG_PRESETS.get(PARENT_OF.get(category_slug), _TAG_PRESETS["bestsellers"]))
    # Optional, real data from catalog_data.py (never invented):
    #   "pages" -> drives the Short / Medium / Long Reads filter
    #   "format" -> Paperback / Hardcover / Audiobook;  "topics" -> extra topic tags
    real_pages = book.get("pages")
    length = "" if not real_pages else "short" if real_pages < 200 else "medium" if real_pages <= 400 else "long"
    topics = [t for t in [category_slug, PARENT_OF.get(category_slug)] + list(book.get("topics", [])) if t]
    return {
        **book,
        "condition": condition,
        "format": (book.get("format") or "").lower(),
        "length": length,
        "topics": topics,
        "discount": discount,
        "savings": savings,
        "img_url": _bare_or_full_img(book["img"]),
        "img_url_small": _bare_or_full_img(book["img"], size=160),
        "category_slug": category_slug,
        "category_title": category_title,
        "tags": tags,
        "rating": rating,
        "rating_full_stars": range(int(rating)),
        "rating_has_half": (rating - int(rating)) >= 0.5,
        "reviews": reviews,
        "pages": real_pages or pages,
        "publisher": _PUBLISHERS[h % len(_PUBLISHERS)],
        "delivery_days": 3 + (h % 3),
        "sample_reviews": _sample_reviews(book_id, tags, condition, category_title),
    }


def find_book(book_id):
    """Looks a book up by id across every category, then the homepage's
    Best Sellers list, and returns it normalised for the detail page."""
    for slug, category in CATEGORIES.items():
        for book in category["own_books"]:
            if book["id"] == book_id:
                return _normalize_book(book, slug, category["title"])
    for book in BEST_SELLERS:
        if book.get("id") == book_id:
            return _normalize_book(book, "bestsellers", "Best Sellers")
    return None


def _norm(text):                          
    text = text.lower().replace("'", "").replace("\u2019", "")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def _book_key(b):
    return (re.sub(r"^the ", "", _norm(b["title"])), _norm(b["author"]))


def related_books(book, limit=5):
    """Amazon/Flipkart-style 'You may also like': same category, best rated first,
    then the parent category if there aren't enough."""
    slug = book["category_slug"]
    my_key = _book_key(book)

    # Homepage best-seller cards have no shelf of their own: find the real one
    if slug not in CATEGORIES:
        for s, c in CATEGORIES.items():
            if any(_book_key(b) == my_key for b in c["own_books"]):
                slug = s
                break

    if slug not in CATEGORIES:
        shelves = [("bestsellers", "Best Sellers", BEST_SELLERS)]
    else:
        shelves = [(slug, CATEGORIES[slug]["title"], CATEGORIES[slug]["books"])]
        parent = CATEGORIES[slug].get("parent")
        if parent in CATEGORIES:
            shelves.append((parent, CATEGORIES[parent]["title"], CATEGORIES[parent]["books"]))

    seen = {my_key}          # never suggest the current book, or the same book twice
    picks = []
    for shelf_slug, shelf_title, pool in shelves:
        shelf = []
        for b in pool:
            key = _book_key(b)
            if key in seen:
                continue
            seen.add(key)
            shelf.append(_normalize_book(b, shelf_slug, shelf_title))
        shelf.sort(key=lambda n: (n["rating"], n["reviews"]), reverse=True)   # best rated first
        picks += shelf
        if len(picks) >= limit:
            break
    return picks[:limit]


def book_detail(request, book_id):
    book = find_book(book_id)
    if not book:
        return render(request, "core/coming_soon.html", {"page_title": "Book"})
    return render(request, "catalog/book_detail.html", {
        "book": book,
        "related": related_books(book),
    })


def category_listing(request, slug):
    category = CATEGORIES.get(slug)
    if not category:
        return render(request, "core/coming_soon.html", {"page_title": slug.replace("-", " ").title()})
    books = [_normalize_book(b, b["_home"], CATEGORIES[b["_home"]]["title"]) for b in category["books"]]
    category = {**category, "books": books}
    return render(request, "catalog/category_listing.html", {"category": category, "slug": slug})


# ---------------------------------------------------------------------------
# Collection pages: Bestsellers, New Arrivals, Pre-Loved, Box Sets.
# They reuse the category page, so every filter / sort / cart feature works.
# Mark books in catalog/catalog_data.py with  "bestseller": True,
# "new_arrival": True  or  "bundle": True  to put them in a collection.
# ---------------------------------------------------------------------------
_COLLECTIONS = {
    "bestsellers": {
        "title": "Bestsellers & Trending",
        "tagline": "The books everyone is reading right now, across every genre.",
    },
    "new-arrivals": {
        "title": "New Arrivals",
        "tagline": "Fresh stock and recent releases, added to the shelves.",
    },
    "pre-loved": {
        "title": "Pre-Loved Books",
        "tagline": "Second-hand reads in great condition, at friendlier prices.",
    },
    "box-sets": {
        "title": "Box Sets & Bundles",
        "tagline": "Series collections, manga box sets and gift-ready bundles.",
    },
    "discount-30": {
        "title": "Up to 30% Off",
        "tagline": "Everyday savings of up to 30% across every genre.",
    },
    "discount-50": {
        "title": "Up to 50% Off",
        "tagline": "Bigger savings of up to 50% across every genre.",
    },
}
_BUNDLE_WORDS = re.compile(r"box(ed)? set|bundle|collection set|omnibus|combo", re.I)


def _all_books():
    """Every book once (not repeated for parent categories), normalised."""
    out = []
    for slug, category in CATEGORIES.items():
        for b in category["own_books"]:
            out.append(_normalize_book(b, slug, category["title"]))
    return out


def _collection_books(slug):
    books = _all_books()
    if slug == "bestsellers":
        picked = [_normalize_book(b, "bestsellers", "Best Sellers") for b in BEST_SELLERS]
        picked += [b for b in books if b.get("bestseller")]
    elif slug == "new-arrivals":
        picked = [b for b in books if b.get("new_arrival")]
        # Nothing flagged yet? Fall back to the most recently added titles
        # (new books are added at the end of each shelf), a couple per shelf.
        recent = []
        for category_slug, category in CATEGORIES.items():
            for b in category["own_books"][-2:]:
                recent.append(_normalize_book(b, category_slug, category["title"]))
        picked += recent[:12 - len(picked)] if len(picked) < 12 else []
    elif slug == "pre-loved":
        picked = [b for b in books if b["condition"].lower() == "pre-loved"]
    elif slug in ("discount-30", "discount-50"):
        # "Up to X% off": every book discounted by more than 0% and at most X%.
        # (Change <= to >= below if you would rather list "X% off or more".)
        limit = int(slug.split("-")[1])
        picked = [b for b in books if b.get("discount") and 0 < b["discount"] <= limit]
        picked.sort(key=lambda b: b["discount"], reverse=True)
    else:  # box-sets
        picked = [b for b in books if b.get("bundle") or _BUNDLE_WORDS.search(b["title"])]
    seen, unique = set(), []
    for b in picked:
        if b["id"] not in seen:
            seen.add(b["id"])
            unique.append(b)
    return unique


def collection(request, slug):
    meta = _COLLECTIONS.get(slug)
    if not meta:
        return render(request, "core/coming_soon.html", {"page_title": slug.replace("-", " ").title()})
    category = {**meta, "count": "", "books": _collection_books(slug)}
    return render(request, "catalog/category_listing.html", {"category": category, "slug": slug})


def search(request):
    query = request.GET.get("q", "").strip()
    results = []
    if query:
        q_lower = query.lower()
        for slug, category in CATEGORIES.items():
            for book in category["own_books"]:
                if q_lower in book["title"].lower() or q_lower in book["author"].lower():
                    results.append(_normalize_book(book, slug, category["title"]))
    return render(request, "catalog/search_results.html", {"query": query, "results": results})


from django.http import JsonResponse


def chat_data(request):
    """Feeds the chatbot widget with every real category and book."""
    cats = [
        {"slug": slug, "title": c["title"], "parent": c.get("parent", "")}
        for slug, c in CATEGORIES.items()
    ]
    books = []
    for slug, c in CATEGORIES.items():
        for b in c["own_books"]:
            n = _normalize_book(b, slug, c["title"])
            books.append({
                "id": b["id"], "title": b["title"], "author": b["author"],
                "price": b["price"], "slug": slug, "parent": c.get("parent", ""),
                "rating": n["rating"],
            })
    return JsonResponse({"cats": cats, "books": books})