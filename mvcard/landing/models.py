from django.db import models


# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=10, verbose_name="Телефон")
    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name="Статус", default=1)

    def __str__(self):
        return self.phone_number


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя статуса")

    def __str__(self):
        return self.name

