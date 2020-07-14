from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Matches(models.Model):
    matcher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='matcher', default='matcher')
    matched = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='matched', default='matched')

    class Meta:
        unique_together = (('matcher', 'matched'))