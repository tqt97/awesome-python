from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    context = {"products": products}
    return render(request, "catalogue/index.html", context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(slug=category_slug).get_descendants(include_self=True)
    )
    context = {"category": category, "products": products}
    return render(request, "catalogue/category.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    context = {"product": product}
    return render(request, "catalogue/single.html", context)
