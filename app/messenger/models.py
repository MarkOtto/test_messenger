from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class MMessage(models.Model):
    user_from = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sender',
        verbose_name="From"
    )
    user_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipient',
        verbose_name="To"
    )
    title = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    body = models.TextField(
        blank=True,
        null=True
    )
    sent = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return(
            datetime.strftime(self.sent, '%y.%m.%d • %H:%M:%S') +
            ' • FROM: ' + str(self.user_from) +
            ' • TO: ' + str(self.user_to) +
            ' • ' + self.title
        )

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'