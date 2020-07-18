import requests
import json
from demo import xld


def token():
    url_dd = 'http://192.168.0.243:8098/login/login'
    header_url = {'Content-Type','application/json'}
    data_url = json.loads(xld.login())
    print(type(data_url))
    data = {"mobile":"0000000027","password":"Fleet@123456"}
    print(type(data))
    rep = requests.post(url_dd,data = data_url)
    rep1 = requests.post(url_dd,data = {"mobile":"0000000027","password":"Fleet@123456"})

    #print(aa)
    bb = rep1.json()['message']
    bb1 = rep1.json()['data']
    print(type(bb1))
    print(bb1)
    cc = bb1['FMS-SESSION-ID']
    print(cc)
    return cc