from rest_framework import serializers
from conversations.models import Conversations
from ErrorMessages import INVALID_DATA_ERR, OBJECT_ALREADY_EXISTS_ERR

class ConversationsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Conversations
		fields = ('time_written', 'message', 'sender', 'receiver')

	def create(self, validated_data):
		message = Conversations.objects.create(**validated_data)
		message.save()
		return message
