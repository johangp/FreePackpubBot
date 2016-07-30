import requests


def get_response():
    response = requests.get('https://www.packtpub.com/packt/offers/free-learning')
    return response.content


def get_book_title(response_soup):
    return "&#8594; " + response_soup.find("div", {"class": "dotd-title"}).h2.text.strip() + ": \n\n"


def get_book_description(response_soup):
    description_html = response_soup.find("div", {"class": "dotd-main-book-summary float-left"})
    description_data = description_html.findAll("div", {"class": ""})
    book = description_data[0].text.strip() + "\n\n"
    if len(description_data) > 1:
        for num, description_key in enumerate(description_data[1].findAll("li")):
            book = book + "&#160; &#160; &#8226; " + description_key.text + "\n"
    return book


def get_book_image(response_soup):
    book_url = 'https:' + response_soup.find("img", {"class": "bookimage"}).get("src")
    return book_url.replace(" ", "%20")
