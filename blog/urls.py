from django.urls import path
from .views import *

urlpatterns = [
 path('', index, name='index'),
 path('contact/', contact, name='contact'),
 path('category/', category, name='category'),
 path('post/', post, name='post'),

]
