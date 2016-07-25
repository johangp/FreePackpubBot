from packtpub_scraper import crawler
from bs4 import BeautifulSoup
from telegram_bot import bot

response_data = crawler.get_response()
response_soup = BeautifulSoup(response_data, 'html.parser')
book_title = crawler.get_book_title(response_soup)
book_description = crawler.get_book_description(response_soup)
book_image_url = crawler.get_book_image(response_soup)

text_to_send = "<strong>" + book_title + ":\n\n </strong><i>" + book_description['description'] + "</i><a href='" + book_image_url + "'>.</a>"

user_list = bot.check_updates()
for user in user_list:
    bot.send_message(user['id'], text_to_send)
