from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class UserProfile(models.Model):
	credentials = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key = True)
	created_at = models.DateTimeField(auto_now_add=True)
	bio = models.CharField(max_length=180)
	occupation = models.CharField(max_length=20)
	birthday = models.DateField()
	twitter_handle = models.CharField(null=True, max_length=20)
	ig_handle = models.CharField(null=True, max_length=20)

	def __str__(self):
		return self.credentials.get_username()

	def get_username(self):
		return self.credentials.get_username()

	def get_profile(self):
		return UserProfile.objects.get(pk=self.credentials.get_username())

