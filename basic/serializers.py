from basic.models import User
from basic.models import Todos
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'

class TodosSerializer(serializers.ModelSerializer):
     class Meta:
         model = Todos
         fields = '__all__'