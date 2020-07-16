from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user_profile.models import UserProfile
from potential_matches.models import PotentialMatches
from django.contrib.auth import get_user_model
from TestConstants import TEST_CREDENTIALS, TEST_CREDENTIALS2, TEST_ACCOUNT, TEST_ACCOUNT2, PROFILE_BASE_URL, TEST_ACCOUNT3, TEST_CREDENTIALS3, POTENTIAL_MATCHES_URL, POTENTIAL_MATCHES_USERNAME_URL, TEST_POTENTIAL_MATCHES

class PotentialMatchesTests(APITestCase):
    def test_create_potential_match(self):
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

    def test_get_potential_match(self):
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

        response = self.client.get(POTENTIAL_MATCHES_USERNAME_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertPotentialMatches(response.data[0], TEST_POTENTIAL_MATCHES['potential_matches'][1])
        self.assertPotentialMatches(response.data[1], TEST_POTENTIAL_MATCHES['potential_matches'][0])

    def assertPotentialMatches(self, actual, expected):
        self.assertEqual(actual['potential_matcher'], expected['potential_matcher']),
        self.assertEqual(actual['potential_matched'], expected['potential_matched'])