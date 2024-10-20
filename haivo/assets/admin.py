from django.contrib import admin
from .models import Asset, Employee, Lending

# Register your models here.
admin.site.register(Asset)
admin.site.register(Employee)
admin.site.register(Lending)