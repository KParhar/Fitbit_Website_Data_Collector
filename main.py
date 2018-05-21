import requests
from lxml import html

loginLink = "https://www.fitbit.com/en-ca/login"
username = "tigrambazzi@gmail.com"
password = "Bhupinder23"

loginPayload = {
	"email": username
	"password": password
	"csrfToken": "c4359d4fcc1c437d8250117845e63a0d"
}

link = "https://www.fitbit.com/"
website = requests.get(link)
htmlText = website.text

print(htmlText)