from django.db import models


# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=255, verbose_name="Имя")
    lastname = models.CharField(max_length=255, verbose_name="Фамилия")
    birth = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

class Transport(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"


class Report(models.Model):
    date = models.DateField(verbose_name="Дата")
    employee = models.ForeignKey(Employee, verbose_name="Сотрудник", on_delete=models.SET_NULL, null=True)
    transport = models.ForeignKey(Transport, verbose_name="Транспорт", on_delete=models.SET_NULL, null=True)
    fuel_dispendsed = models.PositiveIntegerField(verbose_name="Топливо выдано")
    fuel_used = models.PositiveIntegerField(verbose_name="Топливо расходовано")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")

    def __str__(self):
        return self.employee.firstname + " " +  self.employee.lastname + " "  + str(self.date)

    class Meta:
        verbose_name = "Отчёт"
        verbose_name_plural = "Отчёты"