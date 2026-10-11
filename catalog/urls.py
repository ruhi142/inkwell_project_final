from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("chat-data/", views.chat_data, name="chat_data"),        # <-- ADD THIS LINE
    path("collections/<slug:slug>/", views.collection, name="collection"),
    path("book/<str:book_id>/", views.book_detail, name="book_detail"),
    path("<slug:slug>/", views.category_listing, name="category_listing"),
]