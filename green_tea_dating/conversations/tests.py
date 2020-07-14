from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from conversations.models import Conversations
from user_profile.models import UserProfile
from django.contrib.auth import get_user_model
from TestConstants import TEST_CREDENTIALS, TEST_CREDENTIALS2, TEST_ACCOUNT, TEST_ACCOUNT2, TEST_CONVERSATION_BETWEEN, PROFILE_BASE_URL, TEST_CONVERSATION, TEST_CONVERSATION2, CONVERSATION_BASE_URL, CONVERSATION_USERNAME_URL, CONVERSATION_BETWEEN_USER_URL, TEST_CONVERSATION_DELETED, CONVERSATION_BATCH_GET_URL, TEST_CONVERSATION3, TEST_ACCOUNT3, TEST_CREDENTIALS3

# Create your tests here.
class ConversationsTests(APITestCase):
    def test_create_message(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)
        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversations.objects.count(), 1)
        response = Conversations.objects.get(username1=TEST_CONVERSATION['username1'], username2=TEST_CONVERSATION['username2'])
        self.assertMessageInfoIsCorrect(response, TEST_CONVERSATION)

    def test_retrive_message(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversations.objects.count(), 1)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS2['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversations.objects.count(), 2)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(CONVERSATION_BETWEEN_USER_URL, TEST_CONVERSATION_BETWEEN, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertConversationMessages(response.data[1], TEST_CONVERSATION)
        self.assertConversationMessages(response.data[0], TEST_CONVERSATION2)

    def test_delete_message(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversations.objects.count(), 1)

        response = self.client.post(CONVERSATION_BETWEEN_USER_URL, TEST_CONVERSATION_BETWEEN, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.patch(CONVERSATION_USERNAME_URL, response.data[0], format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertConversationMessages(response.data, TEST_CONVERSATION_DELETED)

    # def test_get_all_message(self):
    #     response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT3, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(UserProfile.objects.count(), 3)

    #     user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
    #     self.client.force_authenticate(user=user)

    #     response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Conversations.objects.count(), 1)

    #     response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION3, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Conversations.objects.count(), 2)

    #     user = get_user_model().objects.get(pk=TEST_CREDENTIALS2['username'])
    #     self.client.force_authenticate(user=user)

    #     response = self.client.post(CONVERSATION_BASE_URL, TEST_CONVERSATION2, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Conversations.objects.count(), 3)

    #     user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
    #     self.client.force_authenticate(user=user)

    #     response = self.client.get(CONVERSATION_USERNAME_URL)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 3)


    def assertMessageInfoIsCorrect(self, actual, expected):
        user1 = get_user_model().objects.get(username=actual.username1)
        user2 = get_user_model().objects.get(username=actual.username2)
        self.assertEqual(user1.username, expected['username1'])
        self.assertEqual(user2.username, expected['username2'])
        self.assertEqual(actual.message, expected['message'])

    def assertConversationMessages(self, actual, expected):
        self.assertEqual(actual['username1'], expected['username1'])
        self.assertEqual(actual['username2'], expected['username2'])
        self.assertEqual(actual['message'], expected['message'])