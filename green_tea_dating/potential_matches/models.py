from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class PotentialMatches(models.Model):
    potential_matcher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='potential_matcher', default='potential_matcher')
    potential_matched = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='potential_matched', default='potential_matched')
    swipedOn = models.BooleanField(default=False)
    liked = models.BooleanField()

    class Meta:
        unique_together = (('potential_matcher', 'potential_matched'))