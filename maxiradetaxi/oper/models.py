from django.db import models
from django.utils.timezone import now


class Drivers(models.Model):
    class DriverStatus (models.TextChoices):
        NP = 'Не Працює', 'Не Працює'
        CH = 'Черга', 'Черга'
        OR = 'Замовлення', 'Замовлення'

    car_number = models.CharField('Держномер', max_length=10)
    car_model = models.CharField('Марка', max_length=20)
    car_color = models.CharField('Колір', max_length=20)
    position = models.CharField('Стоянка', max_length=20, blank=True)
    status = models.CharField('Статус', choices=DriverStatus.choices, default=DriverStatus.NP, max_length=10)
    child_seat = models.BooleanField('Крісло')
    trunk = models.BooleanField('Багаж')
    smoking = models.BooleanField('Курець')

    def __str__(self):
        return f'{self.car_number} {self.status}'

    @staticmethod
    def get_absolute_url():
        return f'/operator/'

    class Meta:
        verbose_name = 'Водій'
        verbose_name_plural = 'Водії'


class Orders(models.Model):
    class OrderStatus (models.TextChoices):
        PN = 'Прийнято', 'Прийнято'
        NU = 'Немає', 'Немає'
        VD = 'В дорозі', 'В дорозі'
        CK = 'Чекає', 'Чекає'
        VK = 'Виконнаня', 'Виконнаня'
        VN = 'Виконано', 'Виконано'
        VU = 'Відмінено', 'Відмінено'

    phone = models.DecimalField('Телефон', max_digits=9, decimal_places=0)
    address_from = models.CharField('Звідки', max_length=20)
    address_to = models.CharField('Куди', max_length=20)
    cost = models.FloatField('Ціна', null=True)
    time = models.DateTimeField('Час', default=now)
    status = models.CharField('Статус', choices=OrderStatus.choices, default=OrderStatus.PN, max_length=10)
    comment = models.CharField('Коментар', max_length=30, blank=True)
    driver = models.ForeignKey(
        Drivers,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.phone} {self.status}'

    @staticmethod
    def get_absolute_url():
        return f'/operator/'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
