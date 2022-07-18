from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import Student_Serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_api(request):
    json_data = request.body
    stream_data = io.BytesIO(json_data)  # convert json data to stream_data
    python_data = JSONParser().parse(stream_data)  # convert stream_data to python_data

    # GET REQUEST
    if request.method == 'GET':
        id = python_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Student_Serializer(stu)  # convert python_data into complex data
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = Student_Serializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    # POST REQUEST
    if request.method == 'POST':
        serializer = Student_Serializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            return JsonResponse(res)

        return JsonResponse(serializer.errors, safe=True)

    # PUT REQUEST
    if request.method == 'PUT':
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = Student_Serializer(stu, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated !!'}
            return JsonResponse(res)

        return JsonResponse(serializer.errors, safe=True)

    # DELETE REQUEST
    if request.method == 'DELETE':
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted !!'}
        return JsonResponse(res)
