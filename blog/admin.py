from .models import Product, Cart, Category, Cart_item, Payment
from django.contrib.admin import site
# from models import Post
#
# site.register(Post)

site.register(Product)
site.register(Cart_item)
site.register(Cart)
site.register(Category)
site.register(Payment)
