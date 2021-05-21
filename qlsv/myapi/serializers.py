from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('id', 'mssv', 'name', 'sex', 'faculty')