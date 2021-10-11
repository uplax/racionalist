import uuid
from enum import Enum

from django.db import models
from django.db.models import TextField


class OfferTarget(Enum):
    PRODUCTIVITY_INCREASE = 'Повышение производительности труда'
    COST_REDUCE = 'Снижение затрат'
    WORKING_CONDITION = 'Улучшение организации условий труда'
    QUALITY_IMPROVING = 'Повышение качества продукции'
    PRODUCTION_DOWNLOADS = 'Сокращение простоев оборудования'
    OTHER = 'Прочее'


class OfferPoint(models.Model):
    url = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Идентификатор точки')
    name = models.CharField(max_length=50, verbose_name='Наименование точки')
    description = models.TextField(verbose_name='Описание точки')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Точка подачи предложений'
        verbose_name_plural = 'Точки подачи предложений'
        ordering = ['-created_at']


class Offer(models.Model):
    CHOICES = [
        (tag.value, tag.value) for tag in OfferTarget
    ]

    offer_target = models.CharField(max_length=255, choices=CHOICES)
    target_other = models.TextField(null=True, blank=True)
    short_name = models.CharField(max_length=100, verbose_name='Короткое описание')
    author_first_name = models.CharField(verbose_name='Имя', max_length=20)
    author_second_name = models.CharField(verbose_name='Фамилия', max_length=20)
    author_last_name = models.CharField(verbose_name='Отчество', max_length=20)
    personnel_number = models.CharField(verbose_name='Табельный номер', max_length=10)
    phone = models.TextField(verbose_name='Номер телефона')
    problem_description = models.TextField(verbose_name='Описание проблемы')
    suggestion_for_improvement = models.TextField(verbose_name='Предложение по улучшению')
    expected_result = models.TextField(verbose_name='Ожидаемый результат')

    is_readed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    offer_from = models.ForeignKey(OfferPoint, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
        ordering = ['-created_at']
