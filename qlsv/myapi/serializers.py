from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('id', 'mssv', 'name', 'sex', 'faculty')

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        # token['user_id'] = user.id
        return token