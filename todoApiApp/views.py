from django.shortcuts import render
from rest_framework import generics
from todoApiApp.serializers import TodoDetailSerializer
from todoApiApp.models import Todo
from datetime import datetime

# Create your views here.
class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoDetailSerializer

class TodosListView(generics.ListAPIView):
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()


class TodosListByDateView(generics.ListAPIView):
    serializer_class = TodoDetailSerializer

    def get_queryset(self):

        queryset = Todo.objects.all

        date_from = self.request.parser_context['kwargs']['date_from']
        date_to = self.request.parser_context['kwargs']['date_to']

        date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
        date_to = datetime.strptime(date_to, '%Y-%m-%d').date()

        if date_from and date_to:
            queryset = Todo.objects.filter(date__range=( date_from, date_to))
        return queryset