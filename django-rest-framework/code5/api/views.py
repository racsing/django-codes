from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .models import Student
from .serializers import Student_Serializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

s
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(APIView):
    # GET REQUEST
    def get(self, request, pk=None, format=None):
        id = pk

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = Student_Serializer(stu)  # convert python_data into complex data
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = Student_Serializer(stu, many=True)
        return Response(serializer.data)

    # POST REQUEST
    def post(self, request, format=None):
        serializer = Student_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT REQUEST
    def put(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = Student_Serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Complete Data Updated !!'}
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH REQUEST
    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = Student_Serializer(stu, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Partial Data Updated !!'}
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE REQUEST
    def delete(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted !!'}
        return Response(res)
