from rest_framework import serializers
from conversations.models import Conversations


class ConversationsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Conversations
		fields = ('message', 'username1', 'username2')

	def create(self, validated_data):
		message = Conversations.objects.create(**validated_data)
		message.save()
		return message
