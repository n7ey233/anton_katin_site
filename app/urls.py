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
    #test
    url(r'^test$', views.test, name='test'),
]