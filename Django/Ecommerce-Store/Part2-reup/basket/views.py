from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    context = {'basket': basket}
    return render(request, 'store/basket/summary.html', context)


def basket_add(request):
    basket = Basket(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product_qty = int(request.POST.get('productQty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basket_qty = basket.__len__()
        return JsonResponse({'qty': basket_qty})


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        basket.delete(product=product_id)

        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        return JsonResponse({'qty': basket_qty, 'subtotal': basket_total})


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product_qty = int(request.POST.get('productQty'))
        basket.update(product=product_id, qty=product_qty)

        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        return JsonResponse({'qty': basket_qty, 'subtotal': basket_total})
