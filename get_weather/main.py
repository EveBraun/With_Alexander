import requests
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
    date = soup.find('div', class_="dates short-d").text.split(', ') 
    # <div class="dates short-d"><span>Среда</span>, 19 июня</div>
    day_of_week =date[0]
    day_and_month =date[1]

    table = soup.find('div', class_='weather-short')
    rows = table.find_all('tr')

    # <div class="weather-short"><div class="dates short-d"><span>Четверг</span>, 20 июня</div><div class="pane"></div><table class="weather-today short"></table><table class="weather-today"><tbody><tr class="night"><td class="weather-day">Ночь</td><td class="weather-temperature"><div class="wi n320 wi-v tooltip" title="Местами сильный дождь"></div><span>+14°</span></td><td class="weather-feeling">+14°</td><td class="weather-probability">77%</td><td class="weather-pressure">750</td><td class="weather-wind"><span class="tooltip wwi W" title="западный"></span> <span title=" 7.6 км/ч" class="tooltip ">2.1</span></td><td class="weather-humidity">90%</td></tr><tr class="morning"><td class="weather-day">Утро</td><td class="weather-temperature"><div class="wi d300 wi-v tooltip" title="Преимущественно облачно"></div><span>+15°</span></td><td class="weather-feeling">+15°</td><td class="weather-probability">41%</td><td class="weather-pressure">751</td><td class="weather-wind"><span class="tooltip wwi W" title="западный"></span> <span title=" 11.2 км/ч" class="tooltip ">3.1</span></td><td class="weather-humidity">75%</td></tr><tr class="day"><td class="weather-day">День</td><td class="weather-temperature"><div class="wi d100 wi-v tooltip" title="Незначительная облачность"></div><span>+18°</span></td><td class="weather-feeling">+18°</td><td class="weather-probability">39%</td><td class="weather-pressure">754</td><td class="weather-wind"><span class="tooltip wwi W" title="западный"></span> <span title=" 15.5 км/ч" class="tooltip ">4.3</span></td><td class="weather-humidity">59%</td></tr><tr class="evening"><td class="weather-day">Вечер</td><td class="weather-temperature"><div class="wi n000 wi-v tooltip" title="Ясно"></div><span>+17°</span></td><td class="weather-feeling">+17°</td><td class="weather-probability">1%</td><td class="weather-pressure">755</td><td class="weather-wind"><span class="tooltip wwi W" title="западный"></span> <span title=" 11.9 км/ч" class="tooltip ">3.3</span></td><td class="weather-humidity">
    # print(date)

    row = rows[0]
    time_of_day = row.find('td', class_="weather-day").text
    temperature = row.find('td', class_="weather-temperature").text
    atmosfera = time_of_day.find('div').get('title')
    weather_feeling = row.find('td', class_='weather-feeling').text
    weather_pressure = row.find('td', class_='weather-pressure').text
    wind_direction_kmch = row.find('td', class_='weather-wind').find_all('span')[0].get('title')
    wind_direction_ms =row.find('td', class_='weather-wind').find_all('span')[1].text
    humidity = row.find('td', class_='weather-humidity').text

URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/'
# PATH-params


html = get_html(URL)
get_weather(html)