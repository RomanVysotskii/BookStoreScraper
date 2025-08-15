# Book Store Scraper

Данный проект создан для портфолио.

Программа собирает с сайта https://books.toscrape.com:
- названия книг,
- их стоимость,
- информацию о наличии.

## Для работы используются:
- `fake-useragent` — для генерации случайных User-Agent заголовков при отправке HTTP-запросов
- `requests` — для получения HTML-страниц,
- `BeautifulSoup` (из библиотеки `beautifulsoup4`) — для парсинга и обработки данных,  
- в качестве парсера используется `lxml`.

Результаты работы сохраняются в CSV-файл, который легко открывать в Excel или анализировать программно.

## Установка
```git clone https://github.com/RomanVysotskii/BookStoreScraper
cd project
pip install -r requirements.txt
