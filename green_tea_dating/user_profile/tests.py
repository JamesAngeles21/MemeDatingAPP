from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user_profile.models import UserProfile
from django.contrib.auth import get_user_model
from .test_user_constants import TEST_CREDENTIALS, TEST_ACCOUNT, URL, PROFILE_URL, TEST_UPDATE_BODY, SKIPPABLE_FIELDS 

# Create your tests here.
class AccountTests(APITestCase):
	def test_create_account(self):

		response = self.client.post(URL, TEST_ACCOUNT, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(UserProfile.objects.count(), 1)
		account = UserProfile.objects.get(pk=TEST_CREDENTIALS['username'])
		self.assertAccountInfoIsCorrect(account, TEST_ACCOUNT)

	def test_delete_account(self):
		response = self.client.post(URL, TEST_ACCOUNT, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		response = self.client.delete(PROFILE_URL, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(UserProfile.objects.count(), 0)

	def test_update_account(self):
		response = self.client.post(URL, TEST_ACCOUNT, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		response = self.client.patch(PROFILE_URL, TEST_UPDATE_BODY, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(UserProfile.objects.count(), 1)

		account = UserProfile.objects.get(pk=TEST_CREDENTIALS['username'])
		self.assertAccountInfoIsCorrect(account, TEST_UPDATE_BODY)

	def test_duplicate_account(self):
		response = self.client.post(URL, TEST_ACCOUNT, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		response = self.client.post(URL, TEST_ACCOUNT, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



	def assertAccountInfoIsCorrect(self,actual, expected):
		user = get_user_model().objects.get(username=actual.credentials.username)
		self.assertCredentialsAreCorrect(user)

		for attribute in expected: 
			if (attribute not in SKIPPABLE_FIELDS):
				self.assertEqual(getattr(actual, attribute), expected[attribute])

	def assertCredentialsAreCorrect(self, user):
		self.assertEqual(user.username, TEST_CREDENTIALS['username'])
		self.assertEqual(user.email, TEST_CREDENTIALS['email'])
		self.assertEqual(user.first_name, TEST_CREDENTIALS['first_name'])
		self.assertEqual(user.last_name, TEST_CREDENTIALS['last_name'])
		self.assertTrue(user.check_password(TEST_CREDENTIALS['password']))

