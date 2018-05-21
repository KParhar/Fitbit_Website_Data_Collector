import requests
from lxml import html

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

link = "https://www.fitbit.com/"

result = sRequests.get(link, headers = dict(referer = link))
htmlText = result.text

link = "https://www.fitbit.com/"

result = sRequests.get(link)
htmlText = result.text


print(result.url)