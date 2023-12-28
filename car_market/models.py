from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Car(models.Model):
    TYPE_CAR = (
        ('Спортивная', 'Спортивная'),
        ('Олдовая', 'Олдовая'),
        ('Современная', 'Современная'),
        ('Классическая', 'Классическая')
    )
    title = models.CharField(max_length=100, verbose_name='Укажите название машины')
    description = models.TextField(verbose_name='Дайте описание машины', blank=True)
    photo = models.ImageField(upload_to='cars/', verbose_name='Добавьте фото')
    cost = models.PositiveIntegerField(verbose_name='Укажите цену',
                                       validators=[MinValueValidator(1000),
                                                   MaxValueValidator(30000)])
    car_url = models.URLField(verbose_name='Укажите ссылку на товар', blank=True)
    type_car = models.CharField(max_length=100, choices=TYPE_CAR)
    number_customer = models.CharField(max_length=14, verbose_name='Номер продавца', default='+996')
    oil = models.CharField(max_length=100, verbose_name='Укажите топливо', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

