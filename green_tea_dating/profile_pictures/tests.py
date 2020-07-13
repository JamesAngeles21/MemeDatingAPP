from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from profile_pictures.serializers import ProfilePictureSerializer
from profile_pictures.models import ProfilePicture
from user_profile.serializers import ProfileSerializer
from TestConstants import PROFILE_PICTURE_BASE_URL, TEST_ACCOUNT, TEST_USERNAME, TEST_PICTURES, GET_PROFILE_PICTURES_URL, TEST_CONTENT_URL_6



# Create your tests here.
class ProfilePictureTests(APITestCase):

	def setUp(self):
		serializer = ProfileSerializer(data=TEST_ACCOUNT)
		if serializer.is_valid():
			serializer.save()
		self.user = get_user_model().objects.get(pk=TEST_USERNAME)


	def test_create(self):
		self.client.force_authenticate(user=self.user)
		response = self.client.post(PROFILE_PICTURE_BASE_URL, TEST_PICTURES, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(ProfilePicture.objects.count(), len(TEST_PICTURES))	

	def test_update(self):
		self.client.force_authenticate(user=self.user)
		self.client.post(PROFILE_PICTURE_BASE_URL, TEST_PICTURES, format='json')

		removed_pictures = TEST_PICTURES.copy()
		removed_pictures.pop()
		removed_pictures.pop()		
	
		response = self.client.post(PROFILE_PICTURE_BASE_URL, removed_pictures, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(ProfilePicture.objects.count(), len(removed_pictures))

	def test_retrieve(self):
		self.client.force_authenticate(user=self.user)
		self.client.post(PROFILE_PICTURE_BASE_URL, TEST_PICTURES, format='json')

		response = self.client.get(GET_PROFILE_PICTURES_URL, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		pictures = response.data

		for i in range(len(pictures)):
			self.assertEqual(pictures[i]['path'], TEST_PICTURES[i]['path'])
			self.assertEqual(pictures[i]['picture_number'], TEST_PICTURES[i]['picture_number'])

	def test_upload_more_than_max_allowed(self):
		invalid_picture_amount = TEST_PICTURES.copy()
		invalid_picture_amount.append({'path': TEST_CONTENT_URL_6, 'picture_number': 6})
		self.client.force_authenticate(user=self.user)

		response = self.client.post(PROFILE_PICTURE_BASE_URL, invalid_picture_amount, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)	

	def test_unauth_request(self):
		response = self.client.post(PROFILE_PICTURE_BASE_URL, TEST_PICTURES, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)	