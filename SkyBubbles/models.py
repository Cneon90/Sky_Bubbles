from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    current_price = models.ForeignKey('Price', on_delete=models.SET_NULL, null=True, related_name='current_price')
    image = models.ImageField(upload_to='images')
    # Другие поля

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.product.name} - {self.value}'
