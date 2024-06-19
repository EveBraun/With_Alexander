import requests
import os

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


if os.path.exists('dogs'):
    pass
else:
    os.mkdir('dogs')



def load_image(url, i, breed):
    try:
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            image = response.content

            if os.path.exists(f'dogs/{breed}'):
                pass
            else:
                os.mkdir(f'dogs/{breed}')

            with open(f'dogs/{breed}/image{i}{breed}.jpg', 'wb') as file:
                file.write(image)
        else:
            print('There is a problem')
    except Exception as err:
        print(err)


# with open(f'images/{photo_of_goods.get("alt")}.jpeg', 'ab') as file:       


for i in tqdm(range(1, 3)):
    url_image = get_image_url(URL)
    breed = url_image.split('/')[4]
    print(breed)
    if url_image is not None:
        load_image(url_image, i, breed)
        
    else:
        print('Error')


# breed = 'taksa'
# if os.path.exists(breed):
#     print('Ok')
# else:
#     os.mkdir(breed)
