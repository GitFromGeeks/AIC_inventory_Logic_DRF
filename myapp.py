import requests
import json
URL = "http://127.0.0.1:8000/ordernow/"


data={
    'branch_code' : 'AIC06AH',
    'mobile':'SAMSUNG A51',
    'model': 'SAMA516128B',
    'price': 12000,
    'quantity': 4,
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)