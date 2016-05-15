from .models import Product, Category,Cart_item, Cart
from django.contrib.admin import site
# from models import Post
#
# site.register(Post)

site.register(Product)
site.register(Cart_item)
site.register(Cart)
site.register(Category)
