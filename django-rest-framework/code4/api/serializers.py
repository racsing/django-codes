from .models import Student
from rest_framework import serializers


# Model Serializers
class Student_Serializer(serializers.ModelSerializer):

    # PRIORITY 1 - validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')

    # name = serializers.CharField(read_only=True)
    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        extra_kwargs = {'name': {'read_only': True}}

    # PRIORITY 2 - Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # PRIORITY 3 - Object level validation
    def validate(self, attrs):
        name = attrs.get('name')
        city = attrs.get('city')
        if name.lower() == 'rohit' and city.lower() != 'ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return attrs
