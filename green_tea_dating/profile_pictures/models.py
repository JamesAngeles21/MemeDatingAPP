from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class ProfilePicture(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	path = models.CharField(max_length=150)
	picture_number = models.SmallIntegerField()

	def __str__(self):
		return self.user.username + ": " + number


	class Meta:
		unique_together = (("user", "picture_number"),)