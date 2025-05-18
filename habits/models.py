# flake8: noqa
from django.db import models


class Habit(models.Model):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Пользователь",
    )

    place = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Место",
        help_text="Введи место, в котором необходимо выполнять привычку",
    )

    time_for_habit = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Время",
        help_text="Введи время, когда необходимо выполнять привычку",
    )

    action = models.CharField(
        max_length=150,
        verbose_name="Действие",
        help_text="Введи действие, которое представляет собой привычка",
    )

    good_habit = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        verbose_name="Признак полезной привычки",
        help_text="Привычка, которую можно привязать к выполнению полезной привычки ",
    )

    related_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная привычка",
        help_text="Привычка, которая связана с другой привычкой",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    reword = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Вознаграждение",
        help_text="Укажите, чем можно себя вознаградить после выполнения действия",
    )

    periodicity = models.IntegerField(
        default=1,
        verbose_name="Периодичность",
        null=True,
        blank=True,
        help_text="Укажите периодичность выполнения действия (по умолчанию один раз в день)",
    )

    time_for_action = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Время на действие",
        help_text="Время на выполнение действия",
    )

    public_habit = models.BooleanField(
        default=True, null=True, blank=True, verbose_name="Признак публичности"
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action}"