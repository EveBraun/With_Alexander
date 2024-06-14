import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

# получаем html-страничку по url

def get_html(url):
    user_agent = UserAgent()
    headers = {''}


URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/'
# PATH-params

