from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from user_profile.serializers import ProfileSerializer 
from users.models import CustomUser
from content.models import Content
from swipes.models import Swipe
from TestConstants import SWIPE_BASE_URL, BATCH_CREATE_URL, SINGLE_SWIPE, MULTIPLE_SWIPES, TEST_ACCOUNT, TEST_BATCH_URLS, TEST_USERNAME

# Create your tests here.
class SwipeTests(APITestCase):

	def setUp(self):
		serializer = ProfileSerializer(data=TEST_ACCOUNT)
		if serializer.is_valid():
			serializer.save()
		self.user = get_user_model().objects.get(pk=TEST_USERNAME)
		
		for url in TEST_BATCH_URLS['urls']:
			Content.objects.create(**{'path': url})

	def test_create(self):
		self.client.force_authenticate(user=self.user)
		response = self.client.post(SWIPE_BASE_URL, SINGLE_SWIPE, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), 1)

		swipe = Swipe.objects.get(profile=TEST_USERNAME, content=SINGLE_SWIPE['content'])
		self.assertEqual(swipe.liked, SINGLE_SWIPE['liked'])

	def test_batch_create(self):
		self.client.force_authenticate(user=self.user)	
		response = self.client.post(SWIPE_BASE_URL + BATCH_CREATE_URL, MULTIPLE_SWIPES, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), len(MULTIPLE_SWIPES['swiped_content']))

	def test_update(self):
		self.client.force_authenticate(user=self.user)
		response = self.client.post(SWIPE_BASE_URL, SINGLE_SWIPE, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), 1)

		SINGLE_SWIPE['liked'] = False
		response = self.client.post(SWIPE_BASE_URL, SINGLE_SWIPE, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), 1)

		swipe = Swipe.objects.get(profile=TEST_USERNAME, content=SINGLE_SWIPE['content'])
		self.assertFalse(swipe.liked)


	def test_unauth_request(self):
		response = self.client.post(SWIPE_BASE_URL, SINGLE_SWIPE, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
