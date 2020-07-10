from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Conversations(models.Model):
    time_written = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=280)
    username1 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sender', default='sender')
    username2 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='receiver', default='receiver')

    def createMessage(conversation_data):
       conversation = Conversations.objects.create_user(**conversation_data)
       return conversation

    def findConversations(username1, username2):
        return Conversations.objects.filter(username1=username1, username2=username2)
