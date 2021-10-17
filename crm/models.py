from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from extensions.utils import jalali_converter







class Customer(models.Model):
    name = models.CharField(max_length=200, null=True,verbose_name = "نام")
    phone = models.CharField(max_length=200, null=True,verbose_name = "تلفن")
    additional_information = models.TextField(max_length=1000,null=True, blank=True,verbose_name = "اطلاعات تکمیلی")
    address = models.CharField(max_length=200, null=True,verbose_name = "آدرس")
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name





class Product(models.Model):
    name = models.CharField(max_length=200, null=True,verbose_name = "نام")
    cost = models.FloatField(null=True,verbose_name = "قیمت")
    vendor = models.CharField(max_length=200, null=True,verbose_name = "فروشنده")
    discount = models.IntegerField(default=0,verbose_name = "تخفیف")
    image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.image.url))








class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE,verbose_name = "مشتری")
    product = models.ForeignKey(Product, null=True, on_delete= models.CASCADE,verbose_name = "محصول")
    additional_information = models.TextField(max_length=1000,null=True, blank=True,verbose_name = "اطلاعات تکمیلی")
    prepayment = models.IntegerField(default=0,verbose_name = "پیش پرداخت")
    prepayment_time = models.DateField(null=True,verbose_name = "تاریخ پیش پرداخت")
    delivery_time = models.DateField(null=True,verbose_name = "تاریخ تحویل")
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=(
        ('CANCELED','CANCELED'),
        ('COMPLETED','COMPLETED'),
        ('PAID','PAID'),
        ('PREPAID PAYMENT','PREPAID PAYMENT'),
        ('PENDING PAYMENT','PENDING PAYMENT'),
    ),verbose_name = "وضعیت")


    def j_date_created(self):
        return jalali_converter(self.date_created)




#
