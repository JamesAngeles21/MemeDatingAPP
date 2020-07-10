from rest_framework import serializers
from swipes.models import Swipe


class SwipeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Swipe
		fields = ('profile', 'content', 'liked')

	def create(self, validated_data):
		swipe = Swipe.objects.create(**validated_data)
		swipe.save()
		return swipe

	def update(self, instance, validated_data):
		instance.liked = validated_data['liked']
		instance.save()
		return instance