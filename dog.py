import requests
from time import sleep
TOKEN = "5560601042:AAGmL3FVj2gDu98ssV-uIdLVfROnYmfLKUA"

def getUpd():
    URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(URL)
    s = r.json()
    return s['result']

def getLastUpd(result):
    response = result[-1]
    chat_id = response['message']['chat']['id']
    text = response['message']['text']
    update_id = response['update_id']
    message_id = response['message']['message_id']
    return chat_id, text, update_id, message_id

def sendPhoto(chat_id, text, photo, message_id):
    params = {'chat_id': chat_id, 'photo': photo, 'reply_to_message_id': message_id}
    
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    if text == '/dog':
        r = requests.post(URL, params=params)
        return r.json()
    else: #boshqa text kelib qolganda xatolik bermasligi uchun if else yozdim.
        pass

lastUpdId = -1
while True:
    r = requests.get('https://random.dog/woof.json')
    i = r.json()
    image = i['url']

    result = getUpd()
    chat_id, text, update_id, message_id = getLastUpd(result)
    print(message_id)
    if update_id != lastUpdId:
        sendPhoto(chat_id, text, imgage, message_id)
        lastUpdId = update_id
    sleep(2)
