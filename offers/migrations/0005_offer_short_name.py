# Generated by Django 3.2.8 on 2021-10-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_auto_20211009_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='short_name',
            field=models.CharField(default='alfa', max_length=255, verbose_name='Короткое описание'),
            preserve_default=False,
        ),
    ]
