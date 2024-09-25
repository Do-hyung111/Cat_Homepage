import requests

url = 'http://localhost:8000/index.php'

response = requests.get(url)

print(response)
print(response.text)