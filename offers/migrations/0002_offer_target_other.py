# Generated by Django 3.2.8 on 2021-10-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='target_other',
            field=models.TextField(blank=True, null=True),
        ),
    ]