from .models import Orders, Drivers
from django.forms import ModelForm, TextInput, DateTimeInput, ModelChoiceField, NumberInput


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['phone', 'address_from', 'address_to', 'cost', 'time', 'status', 'comment', 'driver']

        widgets = {
            'phone': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),

            'address_from': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Звідки'
            }),

            'address_to': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Куди'
            }),

            'cost': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна'
            }),

            'time': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Час'
            }),

            'status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус'
            }),

            'comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коментар'
            }),

            #'driver': ModelChoiceField(queryset=Drivers.objects.order_by('status'))
        }
