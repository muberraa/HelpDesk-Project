from django.urls import path
from pages import views
from user.views import login

urlpatterns=[
    path('',views.index,name='index'),
    path('yenitalep',views.yenitalep,name='yenitalep'),
    path('talep',views.talep,name='talep'),
]