from packtpub_scraper import crawler
from bs4 import BeautifulSoup


response_data = crawler.get_response()
response_soup = BeautifulSoup(response_data, 'html.parser')
book_title = crawler.get_book_title(response_soup)
book_description = crawler.get_book_description(response_soup)
book_image_url = crawler.get_book_image(response_soup)
