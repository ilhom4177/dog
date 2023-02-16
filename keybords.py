import os
import requests

TOKEN = '5560601042:AAGmL3FVj2gDu98ssV-uIdLVfROnYmfLKUA'

def sendMessage(chat_id:str,text:str):
    botton1 = {'text':'Dog'}
    botton2 = {'text':'Cat🐱'}
    botton3 = {'text':'Monkey🐵'}
    botton4 = {'text':'elephant🐘'}
    botton5 = {'text':'checkin🐓'}
    botton6 = {'text':'Mouse🐀'}
    botton7 = {'text':'Lion🦁'}

    keyboard = [[botton1],[botton2,botton3,botton4],[botton5,botton6],[botton7]]

    reply_markup = {'keyboard':keyboard}

    payload = {
        'chat_id':chat_id,
        'text':text,
        'reply_markup':reply_markup
    }

    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    response = requests.post(URL, json=payload)
    return response.json()


chat_id = 1046157991
text = "salom"
print(sendMessage(chat_id, text)) 