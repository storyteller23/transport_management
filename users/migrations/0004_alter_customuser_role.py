# Generated by Django 4.1.3 on 2022-11-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_gender_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('B', 'Бухгалтер'), ('D', 'Водитель')], default='D', max_length=1, verbose_name='Должность'),
        ),
    ]
