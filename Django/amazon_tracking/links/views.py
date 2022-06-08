from django.shortcuts import render, redirect

from .forms import AddLinkForm
from .models import Link

from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Create your views here.


def home_view(request):
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = 'Oops.. could not get the name or the price'
        except Exception:
            error = 'Oops.. something went wrong !'
    form = AddLinkForm()

    qs = Link.objects.all()  # query set
    items_no = qs.count()
    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)  # number of discounted items
    context = {
        'qs': qs,
        'items_no': no_discounted,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
    }

    return render(request, 'links/main.html', context)
class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'links/confirm_del.html'
    success_url = reverse_lazy('home')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')