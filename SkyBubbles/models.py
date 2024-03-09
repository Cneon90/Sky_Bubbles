from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    current_price = models.ForeignKey('Price', on_delete=models.SET_NULL, null=True, related_name='current_price',verbose_name='Текущая цена')
    image = models.ImageField(upload_to='images', verbose_name='Фото')
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Вес')
    width = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Ширина')
    length = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Длина')
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')
    deleted = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.product.name} - {self.value}'

# class Ingridient(models.Model):
#     name = models.CharField(max_length=100)
#     color = models.CharField(max_length=50)
#     size_h = models.FloatField()
#     size_w = models.FloatField()
#     weight = models.FloatField()
#     categorys_ingridient_id = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
# class Acceptance(models.Model):
#     ingridient_id = models.IntegerField()
#     user_id = models.IntegerField()
#     storage_id = models.IntegerField()
#     partner_id = models.IntegerField()
#     count = models.IntegerField()
#     price = models.IntegerField()
#     active = models.BooleanField()
#     date = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.ingridient_id} - {self.user_id}"
#
# class Categorys_ingridient(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Partner(models.Model):
#     name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к модели пользователя
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size_h = models.FloatField()
    size_w = models.FloatField()
    weight = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к модели пользователя
    description = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'


class Storage(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к модели пользователя
    description = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class Partner(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к модели пользователя
    description = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Transaction(models.Model):
    price_delivery = models.IntegerField(verbose_name='Стоимость доставки')
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')

    def __str__(self):
        return f'Поставка {self.created_date.strftime("%d.%m.%Y")}'

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class Acceptance(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к модели пользователя
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()
    active = models.BooleanField()
    created_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')
    Transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, verbose_name='Поставка')


    def __str__(self):
        return f"{self.ingredient.name} - {self.user}"

    class Meta:
        verbose_name = 'Приход'
        verbose_name_plural = 'Приходы'


