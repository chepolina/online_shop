from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)


class Cart(models.Model):

    customer = models.ForeignKey("auth.User", default=None)
    date_created = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    invoice = models.IntegerField(default=2)

    def total(self):
        summ = 0
        for obj in self.cart_item_set.all():
            summ += obj.total()
        return summ

# class Customer(models.Model):
#     author = models.ForeignKey('auth.User')
#     email = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     name  = models.CharField(max_length=200)
#     mobile = models.CharField()
#     payment = models.OneToOneField(Payment, on_delete=models.CASCADE, primary_key=False,)

class Payment(models.Model):
    amount = models.IntegerField()
    payment_type = models.CharField(max_length=200)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, primary_key=False, default=None)


class Product(models.Model):
    name = models.CharField(max_length=200)
    published_date = models.DateTimeField(default=timezone.now, editable=True)
    description = models.TextField()
    cost = models.IntegerField()
    weight = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d/", height_field=None, width_field=None, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Cart_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=False,)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def total(self):
        return self.quantity * self.product.cost

