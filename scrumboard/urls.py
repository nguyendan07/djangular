from django.urls import path
from .api import ListApi, CardApi


app_name = 'scrumboard'
urlpatterns = [
    path('lists', ListApi.as_view(), name='lists'),
    path('cards', CardApi.as_view(), name='cards'),
]
