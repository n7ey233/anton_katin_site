from django.shortcuts import render, redirect


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
def order_call(request):
    if request.method == "POST":
        form = order_callForm(request.POST)
        if form.is_valid():
            obje = form.save(commit=False)
            obje.save()
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
        else:
            None
            #redirect na error form.html
    return redirect('applied')
def applied(request):
    return_page = 'app/applied.html'
    return render(request, return_page, {})
#404

#прием заявок на звонок, на запчасть
# Create your views here.
