from rest_framework import serializers
from conversations.models import Conversations


class ConversationsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Conversations
		fields = ('id', 'time_written', 'message', 'username1', 'username2')

	def create(self, validated_data):
		message = Conversations.objects.create(**validated_data)
		message.save()
		return message

	# def update(self, instance, message):
	# 	instance.username1 = validated_data.get('username1', instance.username1)
	# 	instance.username2 = validated_data.get('username2', instance.username2)
	# 	instance.message = validated_data.get('message', instance.message)

	# 	instance.save()
	# 	return instance