from rest_framework import serializers
from django.contrib.auth import get_user_model
from content.models import Content 

class ContentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Content 
		fields = ('path',)

	def create(self, validated_data):
		content = Content.objects.create(**validated_data)
		content.save()
		return content