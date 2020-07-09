TEST_USERNAME = 'test'
TEST_EMAIL = 't@t.com'
TEST_PASSWORD= 't'
TEST_FIRST = 'Tester'
TEST_LAST = 'Testing'

URL = '/profile/'
PROFILE_URL = URL + TEST_USERNAME + "/"

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
