from django import forms
from .models import Order, UserOrder
from django.forms import inlineformset_factory


class UserOrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = [
            'id_name_order', 'name_client',
            'manager_name', 'date_order',
            'ready_product_date_order', 'client_phone_number'
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name', 'status_order', 'amount',
            'price', 'VAT',
        ]




class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "id", "name", "status_order",
            "amount", "price", "price_free_VAT",
            "VAT", "price_with_VAT", "total",
            "total_price_with_VAT", "total_price_ALL"
        )

OrderFormSet = inlineformset_factory(
    UserOrder,
    Order,
    OrderModelForm,
    can_delete=False,
    min_num=2,
    extra=0
)

