from conversations.models import Conversations
from conversations.serializers import ConversationsSerializer
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model

# Create your views here.
class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = Conversations.objects.all()
	serializer_class = ConversationsSerializer
	#permission_classes = (permissions.AllowAny,)

	def retrieve(self, request, username1, username2):
		conversationMessages = get_list_or_404(Conversations, username1=username1, username2=username2) | get_list_or_404(Conversations, username1=username2, username2=username1)
        serializer = ConversationsSerializer(conversationMessages, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def create(self, request, *args, **kwargs):
		serializer = ConversationsSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
