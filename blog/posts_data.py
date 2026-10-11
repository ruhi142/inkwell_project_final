"""
==========================================================================
 INKWELL BLOG — POSTS  (edit this file to add / change articles)
==========================================================================
Add a new post by copying one block inside POSTS, then change:
  slug     - the page address, lowercase-with-dashes  (/blog/<slug>/)
  title    - headline
  kind     - "Review", "Guide" or "List" (shown as a small label)
  date     - "YYYY-MM-DD"
  author   - your name
  book     - optional: {"title": ..., "author": ..., "link": "/category/book/fiction-0/"}
  excerpt  - one or two sentences shown on the blog list page
  body     - a list of paragraphs (each string is one paragraph)

The three posts below are SAMPLES so the Blog page is not empty.
Replace them with your own reviews.
==========================================================================
"""

POSTS = [
    {
        "slug": "why-atomic-habits-still-works",
        "title": "Why Atomic Habits Still Works (and Who It's Not For)",
        "kind": "Review",
        "date": "2026-09-20",
        "author": "Inkwell Editors",
        "book": {"title": "Atomic Habits", "author": "James Clear", "link": "/category/non-fiction/"},
        "excerpt": "A practical, easy-to-finish book on building small routines that last. Here is what it does well and where it repeats itself.",
        "body": [
            "Atomic Habits is built around one simple idea: tiny changes, repeated every day, add up faster than big resolutions that fade by February.",
            "What makes it easy to recommend is how usable it is. Each chapter ends with something you can try that same day, so you are never left with only theory.",
            "It does repeat itself in places, and readers who already follow habit research may find parts familiar. If you are new to the topic, though, it is one of the friendliest starting points.",
            "Read it if you want a clear system for small improvements. Skip it if you are looking for deep science or a one-size-fits-all plan.",
        ],
    },
    {
        "slug": "five-cosy-reads-for-rainy-evenings",
        "title": "Five Cosy Reads for Rainy Evenings",
        "kind": "List",
        "date": "2026-09-12",
        "author": "Inkwell Editors",
        "book": None,
        "excerpt": "Warm, easy-to-sink-into books for when the weather keeps you indoors.",
        "body": [
            "Some books are best read under a blanket with a hot cup of chai. These are the kind we reach for when the rain will not stop.",
            "Look for stories with gentle pacing and characters you want to spend time with. Short chapters help too, because you can stop and start without losing the thread.",
            "Browse our Fiction shelf for contemporary and classic picks, and check the Pre-Loved section for second-hand copies at friendlier prices.",
        ],
    },
    {
        "slug": "how-to-pick-a-pre-loved-book",
        "title": "How to Pick a Pre-Loved Book You'll Be Happy With",
        "kind": "Guide",
        "date": "2026-09-05",
        "author": "Inkwell Editors",
        "book": None,
        "excerpt": "What to check before you buy a second-hand book, from the spine to the smell.",
        "body": [
            "Pre-loved books are a lovely way to read more for less, and a little checking goes a long way.",
            "Look at the spine and the binding first: a book that opens flat without cracking is usually in good shape. Then check for loose pages, heavy highlighting and water marks.",
            "Every pre-loved title on Inkwell is marked with its condition, so you can filter by Pre-Loved on any shelf and compare prices with the new copy.",
        ],
    },
]
