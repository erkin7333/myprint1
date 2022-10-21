from django import forms
from .models import Order, UserOrder, OrderService
from django.forms import inlineformset_factory


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name', 'status_order', 'amount',
            'price', 'VAT',
        ]


class UserOrderForm(forms.ModelForm):
    # orders = forms.MultiValueField(fields=(), widget=OrderForm)

    class Meta:
        model = UserOrder
        fields = "__all__"


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "id", "name", "status_order",
            "amount", "price",
            "VAT"
        )


OrderFormSet = inlineformset_factory(
    UserOrder,
    Order,
    OrderModelForm,
    can_delete=False,
    min_num=2,
    extra=0
)


class OrderServiceForm(forms.ModelForm):
    class Meta:
        model = OrderService
        exclude = ['creat_add']

        widgets = {
            'order_type': forms.Select(attrs={
                'class': 'custom-select',

            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control mt-4',
                'placeholder': 'Имя...'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control mt-3',
                'maxlength': '13',
                'placeholder': 'Телефон...',
                'value': '+998'
            })
        }