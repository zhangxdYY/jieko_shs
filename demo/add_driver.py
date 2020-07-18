import requests
import json
from demo import xld
#获取司机账号
driver1 = json.dumps(xld.driver())
driver = json.loads(driver1)
# driver = xld.driver()
print(type(driver))
print(driver1)
print(type(driver))
print(driver)