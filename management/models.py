from django.db import models
from users.models import CustomUser

# Create your models here.
class Transport(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"


class Report(models.Model):
    date = models.DateField(verbose_name="Дата")
    employee = models.ForeignKey(CustomUser, verbose_name="Сотрудник", on_delete=models.SET_NULL, null=True)
    transport = models.ForeignKey(Transport, verbose_name="Транспорт", on_delete=models.SET_NULL, null=True)
    fuel_dispended = models.PositiveIntegerField(verbose_name="Топливо выдано")
    fuel_used = models.PositiveIntegerField(verbose_name="Топливо расходовано")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")

    def __str__(self):
        if self.employee:
            return self.employee.fullname + ' - ' + str(self.date)
        else:
            return str(self.date)

    class Meta:
        verbose_name = "Отчёт"
        verbose_name_plural = "Отчёты"
        ordering = ('date',)