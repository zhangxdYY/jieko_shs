import requests
import json
denglu_url = r'http://192.168.0.243:8088/login/login'
data_url = {
    "mobile":"0123321123",
    "password":"Fleet@12345"
}
responses = requests.post(denglu_url,data = json.dumps(data_url),headers ={"Content-Type":"application/json"})
# responses.text
a = responses.json()['data']
print(type(a))
b = a['FMS-SESSION-ID']
print(a)
print(b)