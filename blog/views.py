from datetime import date

from django.http import Http404
from django.shortcuts import render

from .posts_data import POSTS


def _prepared():
    posts = []
    for p in POSTS:
        posts.append({**p, "date_obj": date.fromisoformat(p["date"])})
    return sorted(posts, key=lambda p: p["date_obj"], reverse=True)


def blog_list(request):
    return render(request, "blog/blog_list.html", {"posts": _prepared()})


def blog_post(request, slug):
    posts = _prepared()
    post = next((p for p in posts if p["slug"] == slug), None)
    if not post:
        raise Http404("Post not found")
    more = [p for p in posts if p["slug"] != slug][:2]
    return render(request, "blog/blog_post.html", {"post": post, "more": more})
