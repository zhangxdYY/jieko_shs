import requests
import json
import random
denglu_url = r'http://192.168.0.243:8088/login/login'
data_url = {
    "mobile":"0123321123",
    "password":"Fleet@12345"
}


def request1(denglu_url,data_url):
    responses1 = requests.post(denglu_url, data=json.dumps(data_url), headers={"Content-Type": "application/json"})
    return responses1


for i in range(0,2):
    c = str(random.randint(10000, 99999))
    data_url = {
        "mobile": "01233"+c,
        "password": "Fleet@12345"
    }
    print(data_url['mobile'])
    responses1 = request1(denglu_url, data_url)
    a = responses1.json()['message']
    # b = responses1.text
    print(a)
    # print(b)
# responses.text

