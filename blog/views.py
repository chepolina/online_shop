from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    """
    Home page with auth links.
    """
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")


@login_required
def account_profile(request):
    """
    Show user greetings. ONly for logged in users.
    """
    return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('/')

# Create your views here.
def index(request):
    return render(request, "blog/index.html", {})

def shop(request):
    items = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/shop.html", {"items": items})

def shopping_cart(request):
    items = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/shopping_cart.html", {"items": items})


def gift_card(request):
    return render(request, "blog/gift_card.html", {})

def check_out(request):
    return render(request, "blog/check_out.html", {})

def add(request):
    return HttpResponse("Added")

def detail(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    return render(request, 'blog/product.html', {'item': item})

def show_category(request, category):
    items = Product.objects.filter(category=category)
    print(category)
    return render(request, 'blog/shop.html', {'items': items})
