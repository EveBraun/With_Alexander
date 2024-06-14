import requests

cookies = {
    'i': 'q8rm/kC/FP0mo/0sVxaw3+l+3H5fGG3wx0x6lYoB7utX6Yah/mUVyANJ6bcnMfd19edMteGkkpJI4ldYBIHlGmdXw7M=',
    'yandexuid': '4922986131718389474',
    'yashr': '2965809651718389474',
    'bh': 'EkEiR29vZ2xlIENocm9tZSI7dj0iMTI1IiwgIkNocm9taXVtIjt2PSIxMjUiLCAiTm90LkEvQnJhbmQiO3Y9IjI0IioCPzA6CSJXaW5kb3dzIg==',
    'yabs-sid': '10150021718389475',
    'yuidss': '4922986131718389474',
    'ymex': '2033749475.yrts.1718389475',
    'receive-cookie-deprecation': '1',
    'bh': 'Ej8iR29vZ2xlIENocm9tZSI7dj0iMTI1IiwiQ2hyb21pdW0iO3Y9IjEyNSIsIk5vdC5BL0JyYW5kIjt2PSIyNCIaBSJ4ODYiIhAiMTI1LjAuNjQyMi4xNDQiKgI/MDoJIldpbmRvd3MiQggiMTAuMC4wIkoEIjY0IlJcIkdvb2dsZSBDaHJvbWUiO3Y9IjEyNS4wLjY0MjIuMTQ0IiwiQ2hyb21pdW0iO3Y9IjEyNS4wLjY0MjIuMTQ0IiwiTm90LkEvQnJhbmQiO3Y9IjI0LjAuMC4wIiI=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'i=q8rm/kC/FP0mo/0sVxaw3+l+3H5fGG3wx0x6lYoB7utX6Yah/mUVyANJ6bcnMfd19edMteGkkpJI4ldYBIHlGmdXw7M=; yandexuid=4922986131718389474; yashr=2965809651718389474; bh=EkEiR29vZ2xlIENocm9tZSI7dj0iMTI1IiwgIkNocm9taXVtIjt2PSIxMjUiLCAiTm90LkEvQnJhbmQiO3Y9IjI0IioCPzA6CSJXaW5kb3dzIg==; yabs-sid=10150021718389475; yuidss=4922986131718389474; ymex=2033749475.yrts.1718389475; receive-cookie-deprecation=1; bh=Ej8iR29vZ2xlIENocm9tZSI7dj0iMTI1IiwiQ2hyb21pdW0iO3Y9IjEyNSIsIk5vdC5BL0JyYW5kIjt2PSIyNCIaBSJ4ODYiIhAiMTI1LjAuNjQyMi4xNDQiKgI/MDoJIldpbmRvd3MiQggiMTAuMC4wIkoEIjY0IlJcIkdvb2dsZSBDaHJvbWUiO3Y9IjEyNS4wLjY0MjIuMTQ0IiwiQ2hyb21pdW0iO3Y9IjEyNS4wLjY0MjIuMTQ0IiwiTm90LkEvQnJhbmQiO3Y9IjI0LjAuMC4wIiI=',
    'origin': 'https://world-weather.ru',
    'priority': 'u=1, i',
    'referer': 'https://world-weather.ru/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://mc.yandex.ru/watch/25033247?wmode=7&page-url=https%3A%2F%2Fworld-weather.ru%2Fpogoda%2Frussia%2Fsaint_petersburg%2F&charset=utf-8&uah=chu%0A%22Google%20Chrome%22%3Bv%3D%22125%22%2C%22Chromium%22%3Bv%3D%22125%22%2C%22Not.A%2FBrand%22%3Bv%3D%2224%22%0Acha%0Ax86%0Achb%0A64%0Achf%0A125.0.6422.144%0Achl%0A%22Google%20Chrome%22%3Bv%3D%22125.0.6422.144%22%2C%22Chromium%22%3Bv%3D%22125.0.6422.144%22%2C%22Not.A%2FBrand%22%3Bv%3D%2224.0.0.0%22%0Achm%0A%3F0%0Achp%0AWindows%0Achv%0A10.0.0&browser-info=pv%3A1%3Avf%3A1htavzoec9mtiy5ohgcioefk67%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A1360%3Acn%3A1%3Adp%3A0%3Als%3A352624739828%3Ahid%3A383283154%3Az%3A180%3Ai%3A20240614213325%3Aet%3A1718390006%3Ac%3A1%3Arn%3A99636966%3Arqn%3A7%3Au%3A1718389321243361813%3Aw%3A622x915%3As%3A1920x1080x24%3Ask%3A1%3Afp%3A291%3Awv%3A2%3Ads%3A0%2C0%2C106%2C2%2C3%2C0%2C%2C216%2C0%2C%2C%2C%2C328%3Aco%3A0%3Acpf%3A1%3Ans%3A1718390004974%3Agi%3AR0ExLjEuMTk3OTQxNDY2NC4xNzE4Mzg5MzIy%3Aadb%3A1%3Arqnl%3A1%3Ast%3A1718390006%3At%3A%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0%20%D0%B2%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5%20%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F%20-%20%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B%20%D0%B2%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0%2C%20%D1%81%D0%B5%D0%B9%D1%87%D0%B0%D1%81%20(%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C)&t=gdpr(14)clc(0-0-0)rqnt(1)aw(1)rcm(0)cdl(na)eco(21037568)ti(1)',
    cookies=cookies,
    headers=headers,
)

print(response.text)