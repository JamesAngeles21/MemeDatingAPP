from django.db import models
from user_profile.models import UserProfile
from content.models import Content

# Create your models here.
class Swipe(models.Model):
	profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	liked = models.BooleanField()

	def __str__(self):
		return self.profile.credentials.username + ": " + self.content.path +  ": " + self.liked

	class Meta:
		unique_together = (('profile', 'content'),)