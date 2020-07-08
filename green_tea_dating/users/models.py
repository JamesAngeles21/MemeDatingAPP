# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email must be specified")

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

class CustomUser(AbstractUser):
	email = models.EmailField(max_length=254, primary_key=True)

	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'email'

	objects = CustomUserManager()

	def createUser(user_data):
		user = CustomUser.objects.create_user(**user_data)
		return user

	def user_exists(email):
		return CustomUser.objects.filter(email=email).exists()