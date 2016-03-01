from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from .models import Product
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "blog/index.html", {})

def shop(request):
    items = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/shop.html", {"items": items})

def shopping_cart(request):
    return render(request, "blog/shopping_cart.html", {})

def product(request):
    return render(request, "blog/product.html", {})

def gift_card(request):
    return render(request, "blog/gift_card.html", {})

def check_out(request):
    return render(request, "blog/check_out.html", {})

def add(request):
    return HttpResponse("Added")


# class ProductView(TemplateView):
#     template_name = 'product.html'
#
#     #def get(self, request, *args, **kwargs):
#     #    return super(ProductView, self).get(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['item'] = Product.objects.get(id=kwargs['slug'])
#         return context