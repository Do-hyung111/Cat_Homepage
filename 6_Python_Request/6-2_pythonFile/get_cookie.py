import requests

url = 'http://localhost:8000/index.php'
data = {'username': 'babo', 'password': 'babo1234'}

response = requests.post(url, data=data, allow_redirects=False)

cookies = response.cookies

for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")
