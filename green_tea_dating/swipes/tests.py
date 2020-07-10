from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from user_profile.serializers import ProfileSerializer 
from users.models import CustomUser
from content.models import Content
from swipes.models import Swipe
from TestConstants import SWIPE_BASE_URL, BATCH_CREATE_URL, SINGLE_SWIPE, MULTIPLE_SWIPES, TEST_ACCOUNT, TEST_BATCH_URLS

# Create your tests here.
class SwipeTests(APITestCase):

	def setUp(self):
		serializer = ProfileSerializer(data=TEST_ACCOUNT)
		if serializer.is_valid():
			serializer.save()		
		
		for url in TEST_BATCH_URLS['urls']:
			Content.objects.create(**{'path': url})

	def test_create(self):
		response = self.client.post(SWIPE_BASE_URL, SINGLE_SWIPE, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), 1)

		swipe = Swipe.objects.get(profile=SINGLE_SWIPE['profile'], content=SINGLE_SWIPE['content'])
		self.assertEqual(swipe.liked, SINGLE_SWIPE['liked'])

	def test_batch_create(self):
		response = self.client.post(SWIPE_BASE_URL + BATCH_CREATE_URL, MULTIPLE_SWIPES, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), len(MULTIPLE_SWIPES['swiped_content']))

	def test_update(self):
		response = self.client.post(SWIPE_BASE_URL, SINGLE_SWIPE, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), 1)

		SINGLE_SWIPE['liked'] = False
		response = self.client.post(SWIPE_BASE_URL, SINGLE_SWIPE, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Swipe.objects.count(), 1)

		swipe = Swipe.objects.get(profile=SINGLE_SWIPE['profile'], content=SINGLE_SWIPE['content'])
		self.assertFalse(swipe.liked)
