import requests
from lxml import html
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/privacy_policy')
def privacy_policy():
	return render_template('privacy_policy.html')

@app.route('TOS')
def TOS():
	return render_template('TOS.html')

@app.route("callback")
def callback():
	return render_template('callback.html')

if __name__ == '__main__':
    app.run(debug=True)


'''
#IDK IF I NEED THE LOGIN PART
loginLink = "https://www.fitbit.com/en-ca/login"

sRequests = requests.session()

result = sRequests.get(loginLink)
htmlLogin = html.fromstring(result.text)

login = list(set(htmlLogin.xpath("//input[@name='login']/@value")))[0]
includeWorkflow = ""
redirect = ""
switchToNonSecureOnRedirect = list(set(htmlLogin.xpath("//input[@name='switchToNonSecureOnRedirect']/@value")))[0]
csrfToken = list(set(htmlLogin.xpath("//input[@name='csrfToken']/@value")))[0]
disableThirdPartyLogin = list(set(htmlLogin.xpath("//input[@name='disableThirdPartyLogin']/@value")))[0]
email = "tigrambazzi@gmail.com"
password = "Bhupinder23"
rememberMe = "true"
_sourcePage = list(set(htmlLogin.xpath("//input[@name='_sourcePage']/@value")))[0]
__fp = list(set(htmlLogin.xpath("//input[@name='__fp']/@value")))[0]

loginPayload = {
	"login" : login,
	"includeWorkflow" : includeWorkflow,
	"redirect" : redirect,
	"switchToNonSecureOnRedirect" : switchToNonSecureOnRedirect,
	"csrfToken" : csrfToken,
	"disableThirdPartyLogin" : disableThirdPartyLogin,
	"email" : email,
	"password" : password,
	"rememberMe" : rememberMe,
	"_sourcePage" : _sourcePage,
	"__fp" : __fp
}

result = sRequests.post(
	loginLink, 
	data = loginPayload, 
	headers = dict(referer=loginLink)
)

print(result.status_code)

link = "https://api.fitbit.com/1/user/62YB3X/activities/heart/date/today/1d.json"

result = sRequests.get(link)
htmlText = result.text

print(htmlText)
'''