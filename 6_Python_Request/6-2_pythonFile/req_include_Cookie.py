url = 'http://localhost:8000/page-babo.php'

cookies = {
    'user':'babo_bs'
}

response = requests.get(url, cookies=cookies,allow_redirects=False)

print(response.text)
