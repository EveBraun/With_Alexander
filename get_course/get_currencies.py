import requests
import json
 
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


class Parser:
    def __init__(self):
        self.html = None
        self.soup = None
        self.data = None

    def get_html(self, url):
        user_agent = UserAgent()
        headers = {"User-Agent": user_agent.random}
        response = requests.get(url, headers=headers)
        self.html = response.text

    def get_data(self):
        self.soup = bs(self.html, 'html.parser')
        table = self.soup.find('table', class_='js_sortable')
        rows = table.find_all('tr')
        courses_info = {}
        for row in rows[2:]:
            if 'id' in row.attrs:
                continue
            else:
                number_code  = row.find('td', class_='t-center').text.split()[0]
                literal_code = row.find('td', class_='t-center').text.split()[1]
                name  = row.find('td', class_='t-left').text.split('\n')[0]
                course  = row.find('td', class_='t-right').text.strip()

                courses_info[literal_code] = {
                    "number_code": number_code,
                    "name": name,
                    "course": course
                }
        self.data = courses_info

    def print_data(self):
        for item in self.data.items():
            print(item)

    def write_to_file(self):
        pass  

    def get_from_file(self):
        pass        
        



URL = 'https://www.alta.ru/currency/'
courses_parser = Parser()
courses_parser.get_html(URL)
courses_parser.get_data()
courses_parser.print_data()