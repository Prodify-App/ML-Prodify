import requests

response = requests.post("http://localhost:5000/predict", files={'image': open('test/console.jpeg', 'rb')}, data={'category': 'elektronik'})

print(response.json())