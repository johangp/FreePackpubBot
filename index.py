from packtpub_scraper import crawler
from bs4 import BeautifulSoup
from telegram_bot import bot

response_data = crawler.get_response()
response_soup = BeautifulSoup(response_data, 'html.parser')
formatted_book_title = crawler.get_book_title(response_soup)
formatted_book_description = crawler.get_book_description(response_soup)
formatted_book_image_url = crawler.get_book_image(response_soup)

text_to_send = "<strong>" + formatted_book_title + " </strong>" \
               "<i>" + formatted_book_description + "</i>" \
               "<a href='" + formatted_book_image_url + "'>Image Url</a>"

user_list = bot.check_updates()
for user in user_list:
    bot.send_message(user['id'], text_to_send)
