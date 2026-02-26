from django.urls import path
from .views import geopolitical_news

urlpatterns = [
    path("news/", geopolitical_news, name="geopolitical_news"),
]