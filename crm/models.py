from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from extensions.utils import jalali_converter







class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name





class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)
    vendor = models.CharField(max_length=200, null=True)
    discount = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.image.url))

    def j_date_created(self):
        return jalali_converter(self.date_created)






class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=(
        ('CANCELED','CANCELED'),
        ('COMPLETED','COMPLETED'),
        ('REFUNDED','REFUNDED'),
        ('PENDING PAYMENT','PENDING PAYMENT'),
    ))
