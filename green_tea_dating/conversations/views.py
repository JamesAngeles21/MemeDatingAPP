from conversations.models import Conversations
from conversations.serializers import ConversationsSerializer
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.db.models import Q

# Create your views here.
class ConversationsViewSet(viewsets.ModelViewSet):
	queryset = Conversations.objects.all()
	serializer_class = ConversationsSerializer
	permission_classes = (permissions.IsAuthenticated,)

	#delete message (basically update)
	def partial_update(self, request, *args, **kwargs):
		if (request.data['username1'] != request.user.username):
			return Response(status=status.HTTP_400_BAD_REQUEST)
		conversationMessage = get_object_or_404(Conversations, Q(id=request.data["id"]))
		serializer = ConversationsSerializer(conversationMessage, data={'message': 'This message is removed.'}, partial=True)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	#get latest messages STILL NEED TO TEST
	def retrieve(self, request, *args, **kwargs):
		username1 = request.user
		conversationMessages = get_list_or_404(Conversations, Q(username1= username1) | Q(username2= username1))
		serializer = ConversationsSerializer(conversationMessages, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	#get messages between 2
	@action(methods=['post'], detail=False)
	def get_conversation_between_users(self, request, *args, **kwargs):
		if (request.data['username1'] != request.user.username):
			return Response(status=status.HTTP_400_BAD_REQUEST)
		username1 = request.data['username1']
		username2 = request.data['username2']
		conversationMessages = get_list_or_404(Conversations, Q(username1=username1, username2=username2) | Q(username1=username2, username2=username1))
		serializer = ConversationsSerializer(conversationMessages, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	#create message
	def create(self, request, *args, **kwargs):
		serializer = ConversationsSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
