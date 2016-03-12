#from blog.views import ProductView
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^shopping_cart', views.shopping_cart, name='shopping_cart'),
    url(r'^check_out', views.check_out, name='check_out'),
    url(r'^gift_card', views.gift_card, name='gift_card'),
    url(r'^add-to-cart/$', views.add, name='add'),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^shop/(?P<category>[a-z\s]+)/$', views.show_category, name='show_category'),
    url(r'^accounts/logout/$', views.account_logout, name='logout'),
    url(r'^accounts/login/$', views.home, name='login'),
    url(r'^accounts/profile/$', views.account_profile, name='profile'),
    url(r'^$', views.home, name='home')
    #url(r"^item/(?P<slug>.*)", ProductView.as_view(), name='item'),
]