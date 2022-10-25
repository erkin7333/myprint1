from django.db import models
from django.utils.translation import gettext_lazy as _


class Designe(models.Model):
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to="media/service", blank=True, null=True)
    image2 = models.ImageField(upload_to="media/service", blank=True, null=True)
    image3 = models.ImageField(upload_to="media/service", blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Dizayn"


class DigitalPrint(models.Model):
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    on_site_print = models.CharField(max_length=50)
    double_site_print = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/service", blank=True, null=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "Raqamli chop etish"


class LargeFormat(models.Model):
    description = models.TextField(blank=True, null=True)
    product_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to="media/service", blank=True, null=True)
    image2 = models.ImageField(upload_to="media/service", blank=True, null=True)
    image3 = models.ImageField(upload_to="media/service", blank=True, null=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Katta formatda chop etish'



class TextPrint(models.Model):
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(max_length=50, upload_to="media/service", blank=True, null=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "Tekstilni chop etish"

class LaserPrint(models.Model):
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(max_length=50, upload_to="media/service", blank=True, null=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "Lazerni chop etish"

class Type(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xizmat ko'rsatish turlari"

class Image(models.Model):
    type_sevice = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='media/service', blank=True, null=True)

    def __str__(self):
        return str(self.type_sevice)

    class Meta:
        verbose_name = "Xizmat ko'rsatish rasmlari"

class OrderService(models.Model):
    order_type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(_('full_name'), max_length=65)
    phone_number = models.CharField(_('phone_number'), max_length=15)
    creat_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Xizmat ko'rsatish zakazlari"