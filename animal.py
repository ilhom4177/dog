import time
import requests
TOKEN ='5917948695:AAFFicHtinFmKsyPWwQPpjrvlOcXtZZI22g'

def get_updates():
    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/GetUpdates')
    data=r.json()['result'][-1]
    return data
     
def get_dogs():
    r=requests.get('https://random.dog/woof.json/')
    dog=r.json()['url']
    return dog

def get_cats():
    r=requests.get('https://aws.random.cat/meow')
    cat=r.json()['file']
    return cat
     
def send_photo(chat_id,photo):
    param={'chat_id':chat_id,
           'photo':photo
          }

    r=requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',params=param)
    ans=r.json()
    return ans
def send_message(chat_id):
    keyboard=[[{'text':'🐶Dogs'}],[{'text':'😺Cats'}]]
    reply_markup={'keyboard':keyboard}
    param={
        'chat_id':chat_id,
        'text':'Salom botga kelganiz bilan tabriklayman\nBu botda Mushuk va It rasmini olishiz mumkin',
        'reply_markup':reply_markup

    }

    r=requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=param)
    ans=r.json()['result']
    return ans
last_updates_id=-1
while True:
        dogs=get_dogs()
        cats=get_cats()
        upp=get_updates()
        print(upp)
        chat_id=upp['message']['chat']['id']
        text=upp['message']['text']
        updates_id=upp['update_id']

        
        if updates_id!=last_updates_id:
            if text=='/start':
                send_message(chat_id)
            elif text=='🐶Dogs':
                send_photo(chat_id,dogs)
            elif text=='😺Cats':
                 send_photo(chat_id,cats)
            last_updates_id=updates_id
        time.sleep(2)