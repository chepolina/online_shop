from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, Cart, Category, Cart_item, Payment
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.core.cache import cache


def home(request):
    """
    Home page with auth links.
    """
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")


def get_or_creat(request):
    if not Cart.objects.all():
        new_cart = Cart()
        new_cart.customer = request.user
        new_cart.invoice = 50
        new_cart.save()
    elif not Cart.objects.filter(customer=request.user, paid=False).order_by("date_created"):
        new_cart = Cart()
        new_cart.customer = request.user
        new_cart.invoice = Cart.objects.latest("date_created").invoice + 1
        new_cart.save()
    else:
        new_cart = Cart.objects.filter(customer=request.user, paid=False).latest('date_created')
    return new_cart


def delete(request):
    Cart_item.objects.filter(id=int(request.POST.get('item')[4:])).delete()
    return redirect("/shopping_cart/")


def check_out(request):
    return render(request, "blog/check_out.html", {})


@csrf_exempt
def paypal_success(request):
    cart = Cart.objects.filter(customer=request.user, paid=False).latest('date_created')
    cart.paid = True
    cart.save()
    return HttpResponse("Money is mine. Thanks.")


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
    get_or_creat(request)
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
    items = cache.get_or_set('products', Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date'))
    return render(request, "blog/shop.html", {"items": items})

@login_required
def shopping_cart(request):
    """
    Page where we ask user to pay with paypal.
    """
    cart = get_or_creat(request)
    paypal_dict = {
        "business": "chepolina-facilitator@gmail.com",
        "currency_code": "RUB",
        "item_name": "products in socshop",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://chepolina.pythonanywhere.com/payment/success/",
        "cancel_return": "http://chepolina.pythonanywhere.com/shopping_cart/",
        "custom": str(request.user.id)
    }

    # Create the instance.
    cart = Cart.objects.filter(customer=request.user, paid=False).latest("date_created")
    items = cart.cart_item_set.all()
    paypal_dict["amount"] = cart.total()
    paypal_dict["invoice"] = cart.invoice
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict, "items": items, "cart": cart}
    return render(request, "blog/shopping_cart.html", context)


def gift_card(request):
    return render(request, "blog/gift_card.html", {})


def detail(request, product_title):
    item = get_object_or_404(Product, title__iexact=product_title.replace("-", " "))
    return render(request, 'blog/product.html', {'item': item})

def show_category(request, category):
    items = list(Product.objects.filter(category__name=category.replace("-", " ")))
    categories = cache.get_or_set('categories', Category.objects.all())
    return render(request, 'blog/shop.html', {'items': items, 'categories': categories})


@login_required
def add(request):
    cart = get_or_creat(request)
    prod = Cart_item.objects.filter(product_id=int(request.POST.get('item')[4:]), cart=cart)
    if prod:
        prod[0].quantity = prod[0].quantity + 1
        prod[0].save()
    else:
        new_cart_item = Cart_item()
        new_cart_item.cart=cart
        new_cart_item.product=Product.objects.filter(id=int(request.POST.get('item')[4:]))[0]
        new_cart_item.quantity=1
        new_cart_item.save()
    return HttpResponse("Added")
