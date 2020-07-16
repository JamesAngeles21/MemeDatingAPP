from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from conversations.models import Conversations
from user_profile.models import UserProfile
from matches.models import Matches
from swiped_users.models import SwipedUsers
from potential_matches.models import PotentialMatches
from django.contrib.auth import get_user_model
from TestConstants import TEST_CREDENTIALS, TEST_CREDENTIALS2, TEST_CREDENTIALS3, TEST_ACCOUNT, TEST_ACCOUNT2, TEST_ACCOUNT3, PROFILE_BASE_URL, TEST_SWIPED_USERS, TEST_SWIPED_USERS2, TEST_SWIPED_USERS3, SWIPED_USERS_URL, POTENTIAL_MATCHES_URL, TEST_POTENTIAL_MATCHES, MATCHES_USERNAME_URL, TEST_MATCH

# Create your tests here.
class SwipedUsersTests(APITestCase):
    def test_like_swipe(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT3, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 3)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(POTENTIAL_MATCHES_URL, TEST_POTENTIAL_MATCHES, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PotentialMatches.objects.count(), 4)

        response = self.client.post(SWIPED_USERS_URL, TEST_SWIPED_USERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SwipedUsers.objects.count(), 1)
        self.assertEqual(PotentialMatches.objects.count(), 3)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS2['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(SWIPED_USERS_URL, TEST_SWIPED_USERS2, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SwipedUsers.objects.count(), 0)
        self.assertEqual(PotentialMatches.objects.count(), 2)
        self.assertEqual(Matches.objects.count(), 2)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.get(MATCHES_USERNAME_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertMessageInfoIsCorrect(response.data[0], TEST_MATCH)

    def test_unlike_swipe(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT3, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 3)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(POTENTIAL_MATCHES_URL, TEST_POTENTIAL_MATCHES, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PotentialMatches.objects.count(), 4)

        response = self.client.post(SWIPED_USERS_URL, TEST_SWIPED_USERS, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SwipedUsers.objects.count(), 1)
        self.assertEqual(PotentialMatches.objects.count(), 3)

        user = get_user_model().objects.get(pk=TEST_CREDENTIALS2['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(SWIPED_USERS_URL, TEST_SWIPED_USERS3, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SwipedUsers.objects.count(), 0)
        self.assertEqual(PotentialMatches.objects.count(), 2)
        self.assertEqual(Matches.objects.count(), 0)

    def assertMessageInfoIsCorrect(self, actual, expected):
        self.assertEqual(actual['matcher'], expected['matcher'])
        self.assertEqual(actual['matched'], expected['matched'])
