from .models import Student
from rest_framework import serializers


# Model Serializers
class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']