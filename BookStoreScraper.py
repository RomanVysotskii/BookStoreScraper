from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import csv
from urllib.parse import urljoin

#Основные данные для запроса
ua = UserAgent()

base_url = "https://books.toscrape.com"
url = base_url
headers = {
    "Accept": "*/*",
    "User-Agent": ua.chrome
}

#Обработка
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Title', 'Price', 'Availability'])

    #Сбор информации, пока есть книги
    while True:
        #Запрос
        req = requests.get(url, headers=headers)
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, 'lxml')

        books = soup.find_all("div", class_="image_container")

        #Перебор и запись книг на данной странице
        for book in books:
            title = book.find('img')['alt']
            price = soup.find('p', class_='price_color').text.strip()
            availability = soup.find('p', class_='instock availability').text.strip()
            writer.writerow([title, price, availability])

        #Следующая страница, если таковая имеется
        next_page = soup.find('li', class_='next')
        if next_page:
            next_link = next_page.find('a')['href']
            url = urljoin(url, next_link)
        else:
            break