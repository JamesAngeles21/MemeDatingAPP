from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class SwipedUsers(models.Model):
    swiper = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='swiper', default='swiper')
    swiped = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='swiped', default='swiped')
    liked = models.BooleanField(default=False)

    class Meta:
        unique_together = (('swiper', 'swiped'))