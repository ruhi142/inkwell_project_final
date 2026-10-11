"""
Builds the shop's category registry from catalog/catalog_data.py.

You normally never need to edit this file - edit catalog_data.py instead.
"""
from django.utils.text import slugify

from .catalog_data import CATEGORIES as RAW_CATEGORIES


def _with_ids(slug, books):
    """Gives each book a stable id (used by cart / wishlist) and remembers
    which shelf it was defined on ("_home")."""
    out = []
    for i, book in enumerate(books):
        book = dict(book)
        book.setdefault("id", f"{slug}-{i}")
        book["_home"] = slug
        out.append(book)
    return out


def _build():
    registry, parent_of, menu = {}, {}, []
    used = set()

    def claim(slug, what):
        if slug in used:
            raise ValueError(
                f"catalog_data.py: the page address '{slug}' ({what}) is used twice. "
                "Give one of them a different \"slug\"."
            )
        used.add(slug)

    for slug, data in RAW_CATEGORIES.items():
        claim(slug, f"category {data.get('title', slug)}")
        own = _with_ids(slug, data.get("books", []))
        all_books = list(own)
        subs_out = []

        for sub in data.get("subcategories", []):
            if isinstance(sub, str):
                sub = {"name": sub}
            sslug = sub.get("slug") or slugify(sub["name"])
            claim(sslug, f"subcategory {sub['name']}")
            sbooks = _with_ids(sslug, sub.get("books", []))
            registry[sslug] = {
                "title": sub["name"],
                "tagline": sub.get("tagline") or f"Browse {sub['name']} — hand-picked titles from Inkwell.",
                "count": sub.get("count", ""),
                "books": sbooks,
                "own_books": sbooks,
                "parent": slug,
                "parent_title": data["title"],
            }
            parent_of[sslug] = slug
            all_books += sbooks
            subs_out.append({"title": sub["name"], "slug": sslug})

        registry[slug] = {
            **{k: v for k, v in data.items() if k not in ("books", "subcategories")},
            "books": all_books,      # shown on the category page (own + subcategory books)
            "own_books": own,        # used for search / lookups so nothing repeats
            "subcategories": subs_out,
        }
        if data.get("in_menu", True):
            menu.append({"title": data["title"], "slug": slug, "subs": subs_out})

    return registry, parent_of, menu


CATEGORIES, PARENT_OF, MENU = _build()
