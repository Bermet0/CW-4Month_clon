from django.db import models
from django.contrib.auth.models import User



GENDER_TYPE = (
    ("MALE", "M"),
    ("FEMALE", 'Ж'),
    ('UNDEFINED', 'Предпочитаю не отвечать')
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13, default='+996',
                                    verbose_name='Укажите номер телефона')
    date_of_birth = models.DateField(verbose_name='Ваша дата рождения?')
    gender = models.CharField(max_length=100, null=True, choices=GENDER_TYPE,
                              verbose_name='Ваш пол')
