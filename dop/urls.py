from django.urls import path

from .views import *

app_name = 'dop'

urlpatterns = [
   path('News', News, name='News'),
   path('About', About, name='About'),
   path('Contact', Contact, name='Contact'),
]
