from django.db import models

# Create your models here.
class Content(models.Model):
	path = models.CharField(max_length=150, primary_key=True)

	def __str__(self):
		return self.path