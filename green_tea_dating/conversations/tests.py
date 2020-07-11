from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from conversations.models import Conversations
from user_profile.models import UserProfile
from django.contrib.auth import get_user_model
from TestConstants import TEST_CREDENTIALS, TEST_CREDENTIALS2, TEST_ACCOUNT, TEST_ACCOUNT2, PROFILE_BASE_URL, TEST_CONVERSATION, TEST_CONVERSATION2, CONVERSATION_BASE_URL

# Create your tests here.
class ConversationsTests(APITestCase):
    def test_create_message(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)

        response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversations.objects.count(), 1)
        response = Conversations.objects.get(username1=TEST_CONVERSATION['username1'], username2=TEST_CONVERSATION['username2'])
        self.assertMessageInfoIsCorrect(response, TEST_CONVERSATION)

        response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversations.objects.count(), 2)
        response = Conversations.objects.get(username1=TEST_CONVERSATION2['username1'], username2=TEST_CONVERSATION2['username2'])
        self.assertMessageInfoIsCorrect(response, TEST_CONVERSATION2)

    def assertMessageInfoIsCorrect(self, actual, expected):
        self.assertEqual(actual.message, expected['message'])
        # for attribute in expected:
        #     self.assertEqual(getattr(actual, attribute), expected[attribute])