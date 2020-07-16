from rest_framework import serializers
from swiped_users.models import SwipedUsers


class SwipedUsersSerializer(serializers.ModelSerializer):

	class Meta:
		model = SwipedUsers
		fields = ('id', 'swiper', 'swiped', 'liked')

	def create(self, validated_data):
		swiped = SwipedUsers.objects.create(**validated_data)
		swiped.save()
		return swiped