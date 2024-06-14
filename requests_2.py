import requests

from transliterate import translit

def get_gender(name):
    url = f"https://api.genderize.io/?name={name}"

    http_proxy = '51.210.19.141'
    proxies = {
        "http": http_proxy
    }
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    headers = {"User-Agent": user_agent}

    response = requests.get(url, proxies=proxies, headers=headers)
    print(response.json())

    

    data = response.json()
    if data['gender'] == 'female':
        gender = 'женский'
    elif  data['gender'] == 'male':
        gender = 'мужской'
    else:
        gender = 'не определен'

    probability = data['probability']
    # name = translit(value=name, language_code='ru', reversed=False)

    result = f'Имя - {name}, пол - {gender}, вероятность - {probability}'
    print(result)

get_gender('elena')