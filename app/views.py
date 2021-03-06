from django.shortcuts import render, redirect

import requests
import json
from .models import *
from .forms import *

#moi id telegi '405347178'
#id telegi antona '548383851'
id_telegi = '405347178' #id v telege dlya otpravki
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
        # %0A = breakline <br> \n
        name = obje.name
        tel_num = obje.tel_num
        commentary = obje.commentary
        text = 'пришло уведомление заявки на звонок. имя:'+str(name)+' телефон:'+str(tel_num)+' примечание:'+str(commentary)
    #2 == order part
    elif msg_type == 2:
        tel_num = obje.tel_num
        email = obje.email
        parts = obje.parts
        text = 'пришло уведомление заявки на запчасть Телефон: '+str(tel_num)+' , E-mail: '+str(email)+' Необходимые запчасти: '+str(parts)+' url?'
    return text

def send_notification_telegram(text):
    telega_token = '700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg' #token telegi
    case = 1
    if case == 1:
        url = "https://api.telegram.org/bot"+telega_token+"/sendMessage?chat_id="+id_telegi+"&text="+text
        #r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/getUpdates')
        #obrazec
        requests.get(url)
    else:
        None
def order_call(request):
    if request.method == "POST":
        form = order_callForm(request.POST)
        if form.is_valid():
            obje = form.save(commit=False)
            obje.save()
            msg = create_msg(1, obje)
            send_notification_telegram(msg)
        else:
            None
            #redirect na error_form.html
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
    return render(request, return_page, {
    'order_callForm': order_callForm(),
    })
#404
def test(request):
    #init func
    step = 1
    if step == 1:
        r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/getUpdates')
        fulljson = json.loads(r.text)
#прием заявок на звонок, на запчасть
# Create your views here.
