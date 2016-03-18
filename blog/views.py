from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm


def home(request):
    """
    Home page with auth links.
    """
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")

@csrf_exempt
def paypal_success(request):
     """
     Tell user we got the payment.
     """
     return HttpResponse("Money is mine. Thanks.")


@login_required
def paypal_pay(request):
     """
     Page where we ask user to pay with paypal.
     """
     paypal_dict = {
         "business": "acccko-facilitator@gmail.com",
         "amount": "100.00",
         "currency_code": "RUB",
         "item_name": "products in socshop",
         "invoice": "INV-00001",
         "notify_url": reverse('paypal-ipn'),
         "return_url": "http://localhost:8000/payment/success/",
         "cancel_return": "http://localhost:8000/payment/cart/",
         "custom": str(request.user.id)
     }

     # Create the instance.
     form = PayPalPaymentsForm(initial=paypal_dict)
     context = {"form": form, "paypal_dict": paypal_dict}
     return render(request, "payment.html", context)

def homefb(request):
    """
    Home page with auth links.
    """
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/facebook/?next=https://chepolina.pythonanywhere.com/'>login with Facebook</a>")


@login_required
def account_profile(request):
    """
    Show user greetings. ONly for logged in users.
    """
    return redirect("/")


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
