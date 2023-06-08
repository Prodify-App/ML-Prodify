import requests

# response = requests.post("http://34.128.64.94:8080/predict", files={'image': open('test/console.jpeg', 'rb')}, data={'category': 'elektronik'})

response = requests.post("http://localhost:5000/", files={'image': open('test/washing machine.jpeg', 'rb')})

print(response.text)