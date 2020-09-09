from django.contrib import admin
from testapp.models import blorejobs,chennaijobs,hydjobs,punejobs

# Register your models here.

class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligiblity','address','email','phonenumber']


class blorejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligiblity','address','email','phonenumber']


class chennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligiblity','address','email','phonenumber']


class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligiblity','address','email','phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
