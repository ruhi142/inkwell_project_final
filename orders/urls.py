from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("my-orders/", views.my_orders, name="my_orders"),
    path("track/", views.track_order, name="track_order"),
    path("rate/<int:item_id>/", views.rate_item, name="rate_item"),   # <-- ADD THIS
    path("invoice/<str:order_id>/", views.invoice, name="invoice"),
]