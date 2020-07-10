from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from content.models import Content
from TestConstants import CONTENT_BASE_URL, TEST_BATCH_URLS, TEST_CONTENT_URL_1, CONTENT_DELETE_URL, CONTENT_BATCH_DELETE_URL, BATCH_CREATE_URL

# Create your tests here.
class ContentTests(APITestCase):

	def test_create(self):
		response = self.client.post(CONTENT_BASE_URL, {'path': TEST_CONTENT_URL_1}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Content.objects.count(), 1)

		content = Content.objects.get(path=TEST_CONTENT_URL_1)
		self.assertEqual(content.path, TEST_CONTENT_URL_1)

	def test_batch_create(self):
		response = self.client.post(CONTENT_BASE_URL + BATCH_CREATE_URL, TEST_BATCH_URLS, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Content.objects.count(), len(TEST_BATCH_URLS['urls']))

	def test_delete(self):
		response = self.client.post(CONTENT_BASE_URL, {'path': TEST_CONTENT_URL_1}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Content.objects.count(), 1)

		response = self.client.post(CONTENT_DELETE_URL, {'path': TEST_CONTENT_URL_1}, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(Content.objects.count(), 0)

	def test_batch_delete(self):
		response = self.client.post(CONTENT_BASE_URL + 'batch_create/', TEST_BATCH_URLS, format='json')
		self.assertEqual(Content.objects.count(), len(TEST_BATCH_URLS['urls']))

		response = self.client.post(CONTENT_BATCH_DELETE_URL, TEST_BATCH_URLS, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(Content.objects.count(), 0)

	def test_duplicate_create(self):
		response = self.client.post(CONTENT_BASE_URL, {'path': TEST_CONTENT_URL_1}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Content.objects.count(), 1)

		response = self.client.post(CONTENT_BASE_URL, {'path': TEST_CONTENT_URL_1}, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Content.objects.count(), 1)

	def test_duplicate_batch_create(self):
		response = self.client.post(CONTENT_BASE_URL + 'batch_create/', TEST_BATCH_URLS, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Content.objects.count(), len(TEST_BATCH_URLS['urls']))

		response = self.client.post(CONTENT_BASE_URL + 'batch_create/', TEST_BATCH_URLS, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(Content.objects.count(), len(TEST_BATCH_URLS['urls']))
