from django.forms import ModelForm
from .models import talep_detayi,departmanlar
from django.contrib.auth.models import User

class MyYeniTalep(ModelForm):
    class Meta:
        model = talep_detayi
        fields = ['konu','departman','oncelik','icerik']

class Mydepartmant(ModelForm):
    class Meta:
        model = departmanlar
        fields = ['departman']


