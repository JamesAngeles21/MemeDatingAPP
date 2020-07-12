# User Profile Test Constants 

TEST_USERNAME = 'test'
TEST_EMAIL = 't@t.com'
TEST_PASSWORD= 't'
TEST_FIRST = 'Tester'
TEST_LAST = 'Testing'

BATCH_CREATE_URL = 'batch_create/'

PROFILE_BASE_URL = '/profile/'
PROFILE_USERNAME_URL = PROFILE_BASE_URL + TEST_USERNAME + "/"

TEST_CREDENTIALS = {
	'username': TEST_USERNAME,
	'email': TEST_EMAIL,
	'password': TEST_PASSWORD,
	'first_name': TEST_FIRST,
	'last_name': TEST_LAST 
}

TEST_ACCOUNT = {
	'credentials': TEST_CREDENTIALS, 
	"bio": "hello",
	"occupation": "swe",
	"birthday": "1998-10-21"
}

TEST_UPDATE_BODY = {
	"bio": 'updated',
	"occupation": 'doctor',
	"twitter_handle": "@ninja",
	"ig_handle": "@ninjashyper"
}

SKIPPABLE_FIELDS = ['credentials', 'email', 'birthday']

# Content Test Constants

CONTENT_BASE_URL = '/content/'
CONTENT_DELETE_URL = CONTENT_BASE_URL + 'delete/'
CONTENT_BATCH_DELETE_URL = CONTENT_BASE_URL + 'batch_delete/'


TEST_CONTENT_URL_1 = 'https://hello.com'
TEST_CONTENT_URL_2 = 'https://hello1.com'
TEST_CONTENT_URL_3 = 'https://hello2.com'
TEST_CONTENT_URL_4 = 'https://hello3.com'

TEST_BATCH_URLS = {
	'urls': [
		TEST_CONTENT_URL_1,
		TEST_CONTENT_URL_2,
		TEST_CONTENT_URL_3,
		TEST_CONTENT_URL_4
	]
}

# Swipe Test Constants

SWIPE_BASE_URL = '/swipe/'

SINGLE_SWIPE = {
	'content': TEST_CONTENT_URL_1,
	'liked': True
}

MULTIPLE_SWIPES = {
	'swiped_content': [
		{
			'content': TEST_CONTENT_URL_1,
			'liked': True
		},
		{
			'content': TEST_CONTENT_URL_2,
			'liked': True
		},
		{
			'content': TEST_CONTENT_URL_3,
			'liked': False
		}
	]
}
