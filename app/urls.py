from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    #main^ main\about
    url(r'^$', views.main, name='main'),
    #obrabotka zayavki na zvonok
    url(r'^order_call$', views.order_call, name='order_call'),
    #obrabotka zayavki na zapchasti
    url(r'^order_part$', views.order_part, name='order_part'),
    #applied form url, *tipo zayavka prinyata v obrabotku
    url(r'^applied$', views.applied, name='applied'),
    #sozdaniye abonenta
    #url(r'^abonent/create$', views.abonent_create, name='abonent_create'),
    #prosmotr
    #url(r'^abonent/view$', views.abonent_view, name='abonent_view'),
    #redaktirovaniye
    #url(r'^abonent/edit$', views.abonent_edit, name='abonent_edit'),
    #poisk abonenta
    #url(r'^abonent/search$', views.abonent_search, name='abonent_search'),

    #dobavleniye remarki
    #url(r'^add_remark$', views.add_remark, name='add_remark'),
    #dobavleniye excel fila
    #url(r'^add_excel$', views.add_excel, name='add_excel'),
    #url(r'^receive_data$', views.receive_data, name='receive_data'),
]