# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUser(AbstractUser):
	username = models.CharField(max_length=30, primary_key=True) 
	email = models.EmailField(max_length=254, unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	REQUIRED_FIELDS = ["first_name", "last_name"]

	def createUser(user_data):
		user = CustomUser.objects.create_user(**user_data)
		return user

	def user_exists(username):
		return CustomUser.objects.filter(username=username).exists()