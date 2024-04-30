from django.db import models
from tasks.models import Project, Task


# Create your models here.
class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]

    PRIORYTY_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    project = models.ForeignKey(
        Project,

        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,

        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORYTY_CHOICES,
        default='1',
    )




class FeatureRequest(models.Model):

    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]

    PRIORYTY_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    project = models.ForeignKey(
        Project,

        on_delete=models.CASCADE
    )

    task = models.ForeignKey(
        Task,

        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Consideration',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORYTY_CHOICES,
        default='1',
    )