# MemeDatingAPP

## Setup

Clone this project into a local folder

```bash
git clone https://github.com/JamesAngeles21/MemeDatingAPP.git
```

Then navigate to the project folder and create a virtual environment in order to isolate package dependencies locally

```bash
python3 -m venv env
source env/bin/activate # Use env\Scripts\activate for windows
```

Install all necessary libraries and modules (i.e)
```bash
pip3 install django
pip3 install djangorestframework
brew install mysql
pip install pymysql
```

Create a local database using MySQL Workbench and adjust database settings in green_tea_dating/settings.py accordingly

Then properly populate the database with the correct tables and fields by navigating to the outer green_tea_dating folder and call
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
This should have the local server running from terminal

## Usage
In order to add a new table, one must implement Django [Models](https://docs.djangoproject.com/en/3.0/topics/db/models/), [Serializers](https://www.django-rest-framework.org/api-guide/serializers/), and [Viewsets](https://www.django-rest-framework.org/api-guide/viewsets/)
Run the same migration commands above and check on MySQL Workbench to verify that tables were created correctly
Make sure to also add the viewset to the urls.py file in the green_tea_dating folder

## Testing
There are two ways to test your code:

1. Manually Send HTTP requests to server using Postman and verify all actions are correct
2. Write Python tests in the appropriate tests.py file (refer to [this](https://www.django-rest-framework.org/api-guide/testing/))

To manually send HTTP Requests:
- Change the HTTP Request type to the desired one (i.e POST, GET)
- Input the url route that you want
- If sending a POST request, make sure to put data in the raw body similar to
```javascript
{
	"credentials": {
		"email": "test@test.com",
		"password": "j"
	},
	"bio": "hello",
	"occupation": "swe",
	"birthday": "1998-10-21"
}
```