from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<int:id>/', ArticleDetails.as_view(), name='article-details'),
]
