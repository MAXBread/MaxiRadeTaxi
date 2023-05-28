from django.db import models


class Drivers(models.Model):
    car_number = models.CharField('Держномер', max_length=10)
    car_model = models.CharField('Марка', max_length=20)
    car_color = models.CharField('Колір', max_length=20)
    position = models.CharField('Стоянка', max_length=20)
    status = models.CharField('Статус', max_length=10)
    child_seat = models.BooleanField('Крісло')
    trunk = models.BooleanField('Багаж')
    smoking = models.BooleanField('Курець')

    def __str__(self):
        return f'{self.car_number} {self.status}'

    class Meta:
        verbose_name = 'Водій'
        verbose_name_plural = 'Водії'