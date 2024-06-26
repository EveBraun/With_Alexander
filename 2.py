import requests

from tqdm import tqdm

URL = 'https://dog.ceo/api/breeds/image/random'


def get_image_url(url):
    try:
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            data = response.json()
            url_image = data['message']
            return url_image
        else:
            return None
    except Exception as err:
        print(err)
        return None


def load_image(url, i):
    try:
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            image = response.content
            with open(f'image{i}.jpg', 'wb') as file:
                file.write(image)
                print(f'Loaded {i}-file')
        else:
            print('There is a problem')
    except Exception as err:
        print(err)
        

for i in range(1, 11):
    url_image = get_image_url(URL)
    if url_image is not None:
        load_image(url_image, i)
    else:
        print('Error')