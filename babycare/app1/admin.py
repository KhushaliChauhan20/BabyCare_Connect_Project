from django.contrib import admin
from .models import *
# Register your models here.
class parent_(admin.ModelAdmin):
    list_display=['id','name','email','password','par_mobile','address','no_child','child_age']
admin.site.register(parent,parent_)

class service_(admin.ModelAdmin):
    list_display=['id','title','description','img']

admin.site.register(service,service_)

class service_provider_(admin.ModelAdmin):
    list_display=['id','name','pro_email','pro_password','pro_address','experience','photo','age','service','pro_price']

admin.site.register(service_provider,service_provider_)

class book_(admin.ModelAdmin):
    list_display=['id','parent','book_email','service_provider','book_mobile','book_price','book_state','book_city','book_pincode','book_address','transaction','datetime']

admin.site.register(book,book_)