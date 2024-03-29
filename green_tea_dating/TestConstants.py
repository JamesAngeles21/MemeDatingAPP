# User Profile Test Constants

TEST_USERNAME = 'test'
TEST_EMAIL = 't@t.com'
TEST_PASSWORD= 't'
TEST_FIRST = 'Tester'
TEST_LAST = 'Testing'

TEST_USERNAME2 = 'result'
TEST_EMAIL2 = 'r@r.com'
TEST_PASSWORD2 = 'r'
TEST_FIRST2 = 'Resulter'
TEST_LAST2 = 'Resulting'

TEST_USERNAME3 = 'cheater'
TEST_EMAIL3 = 'c@c.com'
TEST_PASSWORD3 = 'c'
TEST_FIRST3 = 'Cheater'
TEST_LAST3 = 'Cheating'

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

TEST_CREDENTIALS2 = {
	'username': TEST_USERNAME2,
	'email': TEST_EMAIL2,
	'password': TEST_PASSWORD2,
	'first_name': TEST_FIRST2,
	'last_name': TEST_LAST2
}

TEST_CREDENTIALS3 = {
	'username': TEST_USERNAME3,
	'email': TEST_EMAIL3,
	'password': TEST_PASSWORD3,
	'first_name': TEST_FIRST3,
	'last_name': TEST_LAST3
}

TEST_ACCOUNT = {
	'credentials': TEST_CREDENTIALS,
	"bio": "hello",
	"occupation": "swe",
	"birthday": "1998-10-21"
}

TEST_ACCOUNT2 = {
	'credentials': TEST_CREDENTIALS2,
	"bio": "hello",
	"occupation": "swe",
	"birthday": "1998-10-21"
}

TEST_ACCOUNT3 = {
	'credentials': TEST_CREDENTIALS3,
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
TEST_CONTENT_URL_5 = 'https://hello4.com'
TEST_CONTENT_URL_6 = 'https://hello5.com'

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

# Conversation Test Constants

CONVERSATION_BASE_URL = '/conversations/'
CONVERSATION_USERNAME_URL = CONVERSATION_BASE_URL + TEST_USERNAME + "/"
CONVERSATION_BETWEEN_USER_URL = CONVERSATION_BASE_URL + 'get_conversation_between_users/'
CONVERSATION_BATCH_GET_URL = CONVERSATION_BASE_URL + '/batch_get/'

TEST_CONVERSATION = {
	"message": "hello this is a test message!",
	"username1": TEST_USERNAME,
	"username2": TEST_USERNAME2
}

TEST_CONVERSATION2 = {
	"message": "wow! I got the message!",
	"username1": TEST_USERNAME2,
	"username2": TEST_USERNAME
}

TEST_CONVERSATION3 = {
	"message": "another message!",
	"username1": TEST_USERNAME,
	"username2": TEST_USERNAME3
}

TEST_CONVERSATION_DELETED = {
	"message": "This message is removed.",
	"username1": TEST_USERNAME,
	"username2": TEST_USERNAME2
}

TEST_CONVERSATION_BETWEEN = {
	"username1" : TEST_USERNAME,
	"username2" : TEST_USERNAME2
}

# Profile Picture Constants
PROFILE_PICTURE_BASE_URL = '/profile_pictures/'
GET_PROFILE_PICTURES_URL = PROFILE_PICTURE_BASE_URL + 'get_profile_pictures/'

TEST_PICTURES = [
	{
		'path': TEST_CONTENT_URL_1,
		'picture_number': 1
	},
	{
		'path': TEST_CONTENT_URL_2,
		'picture_number': 2
	},
	{
		'path': TEST_CONTENT_URL_3,
		'picture_number': 3
	},
	{
		'path': TEST_CONTENT_URL_4,
		'picture_number': 4
	},
	{
		'path': TEST_CONTENT_URL_5,
		'picture_number': 5
	}
]

# Matches Test Constants
MATCHES_BASE_URL = '/matches/'
MATCHES_USERNAME_URL = MATCHES_BASE_URL + TEST_USERNAME + "/"
MATCHES_DELETE_URL = MATCHES_BASE_URL + 'delete_match/'

TEST_MATCH = {
	'matcher': TEST_USERNAME,
	'matched': TEST_USERNAME2
}

TEST_MATCH_REVERSE = {
	'matcher' : TEST_USERNAME2,
	'matched' : TEST_USERNAME
}

TEST_MATCH_ANOTHER = {
	'matcher': TEST_USERNAME,
	'matched': TEST_USERNAME3
}

# Potential Matches Constants
POTENTIAL_MATCHES_URL = '/potential_matches/'
POTENTIAL_MATCHES_USERNAME_URL = POTENTIAL_MATCHES_URL + TEST_USERNAME + "/"

TEST_POTENTIAL_MATCHES = {
	'potential_matches': [
		{
		'potential_matcher': TEST_USERNAME,
		'potential_matched': TEST_USERNAME2},
		{
		'potential_matcher' : TEST_USERNAME,
		'potential_matched' : TEST_USERNAME3}
	]
}

# Swiped Constants
SWIPED_USERS_URL = '/swiped_users/'

TEST_SWIPED_USERS = {
	'swiper': TEST_USERNAME,
	'swiped': TEST_USERNAME2,
	'liked': True
}

TEST_SWIPED_USERS2 = {
	'swiper': TEST_USERNAME2,
	'swiped': TEST_USERNAME,
	'liked': True
}

TEST_SWIPED_USERS3 = {
	'swiper': TEST_USERNAME2,
	'swiped': TEST_USERNAME,
	'liked': False
}