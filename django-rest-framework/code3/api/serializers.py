from .models import Student
from rest_framework import serializers


# All Validators are checked automatically,
# when is_valid() func runs based on the validators priority.
# PRIORITY 1 - validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')


class Student_Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    # name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # POST
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # PUT
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        # print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # PRIORITY 2 - Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # PRIORITY 3 - object level validation
    def validate(self, attrs):
        name = attrs.get('name')
        city = attrs.get('city')

        if name.lower() == 'rohit' and city.lower() != 'ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return attrs
