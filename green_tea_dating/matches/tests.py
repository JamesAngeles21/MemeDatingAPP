from rest_framework import status
from rest_framework.test import APITestCase
from user_profile.models import UserProfile
from matches.models import Matches
from django.contrib.auth import get_user_model
from django.test import TestCase
from TestConstants import TEST_CREDENTIALS, TEST_CREDENTIALS2, TEST_ACCOUNT, TEST_ACCOUNT2, PROFILE_BASE_URL, TEST_MATCH, TEST_MATCH_REVERSE, MATCHES_BASE_URL, MATCHES_DELETE_URL

# Create your tests here.
class MatchesTests(APITestCase):
    def test_create_matches(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)
        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(MATCHES_BASE_URL, TEST_MATCH, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Matches.objects.count(), 2)
        match = Matches.objects.get(matcher=TEST_MATCH['matcher'], matched=TEST_MATCH['matched'])
        self.assertMessageInfoIsCorrect(match, TEST_MATCH)
        match = Matches.objects.get(matcher=TEST_MATCH_REVERSE['matcher'], matched=TEST_MATCH_REVERSE['matched'])
        self.assertMessageInfoIsCorrect(match, TEST_MATCH_REVERSE)

    def test_delete_matches(self):
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(PROFILE_BASE_URL, TEST_ACCOUNT2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 2)
        user = get_user_model().objects.get(pk=TEST_CREDENTIALS['username'])
        self.client.force_authenticate(user=user)

        response = self.client.post(MATCHES_BASE_URL, TEST_MATCH, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Matches.objects.count(), 2)

        response = self.client.post(MATCHES_DELETE_URL, TEST_MATCH_REVERSE, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Matches.objects.count(), 0)

    def assertMessageInfoIsCorrect(self, actual, expected):
        matcher = get_user_model().objects.get(username=actual.matcher)
        matched = get_user_model().objects.get(username=actual.matched)
        self.assertEqual(matcher.username, expected['matcher'])
        self.assertEqual(matched.username, expected['matched'])

