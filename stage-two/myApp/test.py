import requests


response = requests.get('https://hng-myapp.onrender.com/api')
print(response.json())