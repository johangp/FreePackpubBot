import requests


token_bot = 'BOT_TOKEN'
update_id = None


def check_updates():
    global update_id
    method = 'getUpdates'
    response = requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(token_bot, method),
                             data={'offset': update_id}).json()
    users_list = list()
    if response['ok']:
        for message in response['result']:
            if 'chat' in message['message']:
                chat = message['message']['chat']
                users_list.append({'name': chat['first_name'], 'id': chat['id']})

    return users_list


def send_message(chat_id, text):
    method = 'sendMessage'
    response = requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(token_bot, method),
                             data={'chat_id': chat_id, 'text': text}).json()
    print response


while True:
    for user in check_updates():
        send_message(user['id'], 'Hi!' + user['name'])
