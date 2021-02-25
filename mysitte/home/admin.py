from django.contrib import admin
from home.models import a    #importing class contact


# Register your models here.
admin.site.register(a)   #manually added


admin.site.site_header = "Girija Admin"
admin.site.index_title = "Welcome to Girija Tutorial"
admin.site.site_title = "Girija Tutorial"