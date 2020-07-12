from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Matches(models.Model):
    user1 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user2')

    class Meta:
        unique_together = (('user1', 'user2'))