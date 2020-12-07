from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth



class departmanlar(models.Model):
    departman = models.CharField(max_length=50)

    def __str__(self):
       return self.departman






# Create your models here.
class talep_detayi(models.Model):
    ÖNCELİK = (
        ('Düşük', 'Düşük'),
        ('Orta', 'Orta'),
        ('Yüksek', 'Yüksek'),
    )
    adsoyad = models.OneToOneField(User, on_delete=models.CASCADE)
    # id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    konu = models.CharField(max_length=100)
    departman = models.ForeignKey(departmanlar, on_delete=models.CASCADE)
    oncelik = models.CharField(max_length=10, choices=ÖNCELİK)
    icerik = models.TextField(max_length=500)

    def __str__(self):
        return self.konu

    
        
