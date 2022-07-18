from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# POST
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream_data = io.BytesIO(json_data)  # convert json data to stream_data
        python_data = JSONParser().parse(stream_data)    # convert stream_data to python_data
        serializer = StudentSerializer(data=python_data)     # convert python_data into complex data

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            js_data = JSONRenderer().render(res)
            return HttpResponse(js_data, content_type='application/json')
        else:
            js_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(js_data, content_type='application/json')


# GET
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # Serializing: converting complex data to python datatypes
    serial = StudentSerializer(stu)
    # Converting data into json
    json_data = JSONRenderer().render(serial.data)
    # returning json response
    return HttpResponse(json_data, content_type='application/json')


# GET
def all_student_detail(request):
    stu = Student.objects.all()

    # Serializing: converting complex data to python datatypes
    serial = StudentSerializer(stu, many=True)

    # returning json response
    return JsonResponse(serial.data, safe=False)