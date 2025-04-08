# admin.py
from django.contrib import admin
from .models import Form 

admin.site.register(Form)

# super user : admin = admin, pass = admin