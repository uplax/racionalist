# Generated by Django 3.2.8 on 2021-10-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_offer_is_readed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='author_first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='author_last_name',
            field=models.CharField(max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='author_second_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
    ]
