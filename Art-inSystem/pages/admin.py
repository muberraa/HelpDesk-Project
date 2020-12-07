from django.contrib import admin
from .models import departmanlar
from .models import talep_detayi


# Register your models here.
admin.site.register(departmanlar)
admin.site.register(talep_detayi)