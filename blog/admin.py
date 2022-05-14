from django.contrib import admin
from .models import *



#-----------------------------------------------
class Post_categoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Post_category,  Post_categoryAdmin)
admin.site.register(Post, PostAdmin)
#---------------------------------------------------------





