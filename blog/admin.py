from django.contrib import admin
from .models import Product
from django.contrib.admin import site
# from models import Post
#
# site.register(Post)

admin.site.register(Product)
