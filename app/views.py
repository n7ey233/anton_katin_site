from django.shortcuts import render, redirect

import requests
import json
from .models import *
from .forms import *


def main(request):
    #post_list = post.objects.all().order_by('-created_date')
    nav_bar = 1
    return_page = 'app/main.html'
    show_form = True
    if request.GET.get('q', '') != '':
        action = request.GET.get('q').lower()
        if action == 'доставка':
            nav_bar = 2
            return_page = 'app/dostavka.html'
        elif action == 'контакты':
            nav_bar = 4
            return_page = 'app/contacts.html'
        elif action == 'полезная_информация':
            nav_bar = 5
    #tut tol'ko otobrazhaem vse posti iz lichnogo dnevnika
    return render(request, return_page,{
        'nav_bar' : nav_bar,
        'order_partForm': order_partForm(),
        'order_callForm': order_callForm(),
        'show_form': show_form,
        })

def create_msg(msg_type, obje):
    #1 == call
    if msg_type == 1:
        obje
        text = 'пришло уведомление заявки на звонок имя телефон примечание'
    #2 == order part
    elif msg_type == 2:
        text = 'пришло уведомление заявки на запчасть имя телефон запчасть юрл на просмотр'
    return text

def send_notification_telegram(text):
    id_telegi = '405347178' #id v telege dlya otpravki
    telega_token = '700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg'#token telegi
    url = "https://api.telegram.org/bot"+telega_token+"/sendMessage?chat_id="+id_telegi+"&text="+text
    #r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/getUpdates')
    #obrazec
    r = requests.get(url)

def order_call(request):
    if request.method == "POST":
        form = order_callForm(request.POST)
        if form.is_valid():
            obje = form.save(commit=False)
            obje.save()
            msg = create_msg(2, obje)
            send_notification_telegram(msg)
        else:
            None
            #redirect na error form.html
    return redirect('applied')

def order_part(request):
    if request.method == "POST":
        form = order_partForm(request.POST)
        if form.is_valid():
            obje = form.save(commit=False)
            obje.save()
            msg = create_msg(2, obje)
            send_notification_telegram(msg)
        else:
            None
            #redirect na error form.html
    return redirect('applied')
def applied(request):
    return_page = 'app/applied.html'
    return render(request, return_page, {})
#404
def test(request):
    #init func
    step = 1
    if step == 1:
        r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/getUpdates')
        fulljson = json.loads(r.text)
        r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/getUpdates')
        #https://api.telegram.org/bot$TOKEN/
         #poluchaemiy object
        #'{"ok":true,"result":[{"update_id":999597240,\n"message":{"message_id":1,"from":{"id":405347178,"is_bot":false,"first_name":"Vladislav","language_co
        #de":"ru"},"chat":{"id":405347178,"first_name":"Vladislav","type":"private"},"date":1543473969,"text":"/start","entities":[{"offset":0,"length":6,"ty
        #pe":"bot_command"}]}}]}'
    elif step == 2:
        None
#прием заявок на звонок, на запчасть
# Create your views here.
