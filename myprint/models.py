import datetime

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import datetime


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        user = self.model(
            first_name=first_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, phone_number, password):
        user = self.create_user(first_name, phone_number, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first_name'), max_length=64, blank=True)
    full_name = models.CharField(_('full_name'), max_length=64, blank=True)
    phone_number = models.IntegerField(_('phone_number'), blank=True, unique=True)
    email = models.EmailField(verbose_name='email address', null=True, max_length=25)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']

    objects = MyUserManager()

    def get_full_name(self):
        return self.full_name

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self) -> str:
        return self.full_name

    def save(self, *args, **kwargs):
        # password = self.password
        # self.set_password(password)
        return super(User, self).save(*args, **kwargs)



# detail product
class InfoProduct(models.Model):
    size = models.CharField(_('size'), max_length=65)
    element = models.CharField(_('element'), max_length=65)

    def __str__(self):
        return self.size


class Category(models.Model):
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True, default=None)
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/category_image', blank=True, null=True)


    @property
    def children(self):
        return Category.objects.filter(parent=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

# Product
class Product(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/product')
    info_product = models.ForeignKey(InfoProduct, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    vendor_code = models.CharField(max_length=20)
    description = models.TextField(_('description'))

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"


class Product_Orders(models.Model):
    name = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.name} {self.vendor_code} {self.phone}"

    class Meta:
        verbose_name = "Maxsulot zakazi"
        verbose_name_plural = "Maxsulot zakazlari"


class Settings(models.Model):
    key = models.CharField(max_length=50, primary_key=True)
    value = models.TextField()
    class Meta:
        verbose_name = "Sozlama"
        verbose_name_plural = "Sozlamalar"


#  About model
class About(models.Model):
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Biz Haqimizda"

# About uchun rasmlar turadigan model
class AboutImage(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to='media/about', blank=True, null=True)
    def __str__(self):
        return self.name



# Reklama , Poligrafia, Suviner
class TypeService(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(upload_to="media/typeserveis")

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Xizmat turi"


class MenuService(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/menuservice')
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Menyu Xizmati"




class Sponsors(models.Model):
    image = models.ImageField(_('image'), upload_to='media/sponsor')

    def __str__(self) -> str:
        return str(self.image)


class UserOrder(models.Model):
    id_name_order = models.CharField(max_length=300)
    name_client = models.CharField(max_length=65)
    client_phone_number = models.CharField(max_length=65)
    manager_name = models.CharField(max_length=65)
    date_order = models.DateTimeField(auto_now_add=True)
    ready_product_date_order = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.id_name_order

    class Meta:
        db_table = "userorders"
        verbose_name = "Foydalanuvchi zakazi"
        verbose_name_plural = "Foydalanuvchi zakazlari"


class Order(models.Model):
    Product_Status = (
        ('шт', 'шт'),
        ('усл', 'усл'),
    )
    name = models.CharField(max_length=65)
    status_order = models.CharField(max_length=20, choices=Product_Status, default='шт', null=True, blank=True)
    amount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    price_free_VAT = models.FloatField(null=True)
    VAT = models.FloatField(null=True)
    price_with_VAT = models.FloatField(null=True)
    total = models.FloatField(null=True)
    total_price_with_VAT = models.FloatField(null=True)
    total_price_ALL = models.FloatField(null=True)
    order = models.ForeignKey(UserOrder, verbose_name='Zakazlar', related_name="orderform", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "orderform"
        verbose_name = "Zakaz"
        verbose_name_plural = "Zakazlar"



