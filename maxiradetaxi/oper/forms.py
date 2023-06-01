from .models import Orders, Drivers
from django.forms import ModelForm, TextInput, DateTimeInput, ModelChoiceField, NumberInput, CheckboxInput, ChoiceField


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['phone', 'address_from', 'address_to', 'cost', 'time', 'status', 'comment', 'driver']

        driver = ModelChoiceField(queryset=Drivers.objects.all())

        status = ChoiceField()

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

            # 'status': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Статус'
            # }),

            'comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коментар'
            })
        }


class DriverForm(ModelForm):
    class Meta:
        model = Drivers
        fields = ['car_number', 'car_model', 'car_color', 'position', 'status', 'child_seat', 'trunk', 'smoking']

        status = ChoiceField()

        widgets = {
            'car_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Держномер'
            }),

            'car_model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка'
            }),

            'car_color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Колір'
            }),

            'position': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоянка'
            }),

            # 'status': ChoiceField(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Статус'
            # }),

            'child_seat': CheckboxInput(attrs={}),

            'trunk': CheckboxInput(attrs={}),

            'smoking': CheckboxInput(attrs={})
        }
