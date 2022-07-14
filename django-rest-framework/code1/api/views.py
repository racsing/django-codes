from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # Serializing: converting complex data to python datatypes
    serial = StudentSerializer(stu)
    # Converting data into json
    json_data = JSONRenderer().render(serial.data)
    # returning json response
    return HttpResponse(json_data, content_type='application/json')


def all_student_detail(request):
    stu = Student.objects.all()

    # Serializing: converting complex data to python datatypes
    serial = StudentSerializer(stu, many=True)

    # returning json response
    return JsonResponse(serial.data, safe=False)