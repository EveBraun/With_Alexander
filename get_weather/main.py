import requests
import json
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

# получаем html-страничку по url

def get_html(url):
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    return response.text


def get_weather(html:str):
    # создаем объект html-страницы в формате bs
    soup = bs(html, 'html.parser')
    date = soup.find('div', class_="dates short-d") 
    # <div class="dates short-d"><span>Среда</span>, 19 июня</div>
    if date:
        date = soup.find('div', class_="dates short-d").text.split(', ')
    else:
        date = ['None', 'None']

    day_of_week =date[0]
    day_and_month =date[1]

    table = soup.find('table', class_='weather-today short')
    rows = table.find_all('tr')
    weather_today = {"day_of_week": day_of_week, 
                     'day_and_month': day_and_month}

   
    for row in rows:
        weather_day = row.find('td', class_="weather-day").text
        temperature = row.find('td', class_="weather-temperature").text
        # atmosfera = weather_day.find('div').get('title')
        weather_feeling = row.find('td', class_='weather-feeling').text
        weather_pressure = row.find('td', class_='weather-pressure').text
        
        wind_direction = row.find('td', class_='weather-wind').find_all('span')[0].get('title')
        wind_speed_ms =row.find('td', class_='weather-wind').find_all('span')[1].text
        humidity = row.find('td', class_='weather-humidity').text

        weather_today[weather_day] = {
            'temperature': temperature,
            # 'atmosfera': atmosfera,
            'weather_feeling': weather_feeling,
            'weather_pressure': weather_pressure,
            'wind': {
                'wind_direction': wind_direction,
                'wind_speed_ms': wind_speed_ms,
            },
            'humidity': humidity
        }
    return weather_today

URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/'
# PATH-params


html = get_html(URL)
weather_info = get_weather(html)
weather_json = json.dumps(weather_info, ensure_ascii=False)
print(weather_json)


# что-то тут не работает