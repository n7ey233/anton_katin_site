import requests
import json
#https://www.forsomedefinition.com/automation/creating-telegram-bot-notifications/
#esli nado poluchit' id dlya otpravki

def create_msg(msg_type):
    #1 == call
    if msg_type == 1:
        text = 'пришло уведомление заявки %0Aна звонок имя телефон %0Aпримечание'
    #2 == order part
    elif msg_type == 2:
        text = 'пришло уведомление заявки на запчасть имя телефон запчасть юрл на просмотр'
    #print(text)
    return text
def send_notification_telegram(text):
    id_telegi = '405347178' #id v telege dlya otpravki
    telega_token = '700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg' #token telegi
    case = 1
    if case == 1:
        url = "https://api.telegram.org/bot"+telega_token+"/sendMessage?chat_id="+id_telegi+"&text="+text
        #r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/getUpdates')
        #obrazec
        requests.get(url)
    else:
        None
if True:
#if False:
    r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/getUpdates')
    print(r.text)
else:
    msg = create_msg(2)
    print(msg)
    send_notification_telegram(msg)