from django.db import models
from user_profile.models import UserProfile
from content.models import Content
from django.contrib.auth import get_user_model

# Create your models here.
class Swipe(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	liked = models.BooleanField()

	def __str__(self):
		return self.user.username + ": " + self.content.path +  ": " + self.liked

	class Meta:
		unique_together = (('user', 'content'),)