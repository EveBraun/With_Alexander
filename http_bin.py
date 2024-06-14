# Если сайт имеет апи
# Парсинг - если нет апи

import requests
import json

from fake_useragent import UserAgent

# создали экземпляр класса UserAgent
# чтобы не показывать сайту, что работает скрипт
user_agent = UserAgent()
# print(user_agent.random)

URL = 'http://httpbin.org/post'

headers = {'Content-Type': 'application/json'}
data = {'login': "user", 'password': "qwerty"}

response = requests.post(URL, json=json.dumps(data), headers=headers)

print(response.json())

# print(type(data))  #<class 'dict'>
# print(type(json.dumps(data))) #<class 'str'>

# loads - обратно в json
# сериализация - из объекта получаем json