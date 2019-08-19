from rest_framework import serializers
from todoApiApp.models import Todo



class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'