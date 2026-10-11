from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST

from .models import Order, OrderItem


@login_required(login_url="core:home")
@never_cache
def my_orders(request):
    orders = request.user.orders.all()
    return render(request, "orders/my_orders.html", {"orders": orders})


@login_required(login_url="core:home")
@never_cache
def track_order(request):
    order_id = request.GET.get("order_id", "").strip()
    order = None
    not_found = False

    if order_id:
        order = Order.objects.filter(order_id__iexact=order_id, user=request.user).first()
        not_found = order is None
    # No order_id in the URL yet -> don't show anything until the user
    # actually searches. (Previously this fell back to showing the user's
    # most recent order automatically, even before they'd typed anything.)

    return render(request, "orders/track_order.html", {
        "order": order,
        "not_found": not_found,
        "order_id_searched": order_id,
        "searched": bool(order_id),
    })


@login_required(login_url="core:home")
@never_cache
def invoice(request, order_id):
    order = get_object_or_404(Order, order_id__iexact=order_id, user=request.user)
    return render(request, "orders/invoice.html", {"order": order})

@login_required(login_url="core:home")
@require_POST
def rate_item(request, item_id):
    item = get_object_or_404(OrderItem, pk=item_id, order__user=request.user)
    try:
        rating = int(request.POST.get("rating", ""))
    except ValueError:
        return JsonResponse({"ok": False, "error": "Invalid rating"}, status=400)
    if not 1 <= rating <= 5:
        return JsonResponse({"ok": False, "error": "Rating must be 1-5"}, status=400)
    item.rating = rating
    item.save(update_fields=["rating"])
    return JsonResponse({"ok": True, "rating": rating})