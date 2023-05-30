# MaxiRadeTaxi
## Послідовність стутусу замовлення
1. **Прийнято** - Замовленя прийнято оператором
2. **Немає** - Нема вільних водіїв
3. **В дорозі** - Водій в дорозі до клієнта
4. **Чекає** - Водій чекає за адресою 
5. **Виконнаня** - Водій виконує замовлення
6. **Виконано** - Водій виконав замовлення
7. **Відмінено** - Водій/Клієнт відмовився від замовлення

## Статус водія 
1. **Не Працює** - Водій не на роботі
2. **Черга** - Очікує замовлення
3. **Замовлення** - Виконує замовлення

## Таблиці бази данних
### Ordrer(Замовлення)
- phone = models.DecimalField('Телефон', max_digits=9, decimal_places=0)
- address_from = models.CharField('Звідки', max_length=20)
- address_to = models.CharField('Куди', max_length=20)
- cost = models.FloatField('Ціна', null=True)
- time = models.DateTimeField('Час', default=now)
- status = models.CharField('Статус', max_length=10)
- comment = models.CharField('Коментар', max_length=30, blank=True)
- driver = models.ForeignKey(Drivers, on_delete=models.DO_NOTHING, blank=True, null=True)

### Drivers(Водії)
- car_number = models.CharField('Держномер', max_length=10)
- car_model = models.CharField('Марка', max_length=20)
- car_color = models.CharField('Колір', max_length=20)
- position = models.CharField('Стоянка', max_length=20, blank=True)
- status = models.CharField('Статус', max_length=10)
- child_seat = models.BooleanField('Крісло')
- trunk = models.BooleanField('Багаж')
- smoking = models.BooleanField('Курець')




