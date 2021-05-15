from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('articles/', article_list, name='article-list'),
    path('articles/<int:pk>/', article_details, name='article-details'),
]
