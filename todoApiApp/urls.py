from django.contrib import admin
from django.urls import path , include
from todoApiApp.views import *

app_name='todoApiApp'
urlpatterns = [
    path('create/' , TodoCreateView.as_view()),
    path('all/' , TodosListView.as_view()),
    path('id/<int:pk>/' , TodoDetailView.as_view()),
    path('filter/<str:date_from>/<str:date_to>/' , TodosListByDateView.as_view()),
]
