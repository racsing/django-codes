from django.shortcuts import render
from .models import Student
from .serializers import Student_Serializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.generics import GenericAPIView


# GenericAPIView and Model Mixin


class LC_StudentApi(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

    def get(self, request, *args, **kwargs):
        ''' List All data'''
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ''' Post data '''
        return self.create(request, *args, **kwargs)


class RUD_StudentApi(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

    def get(self, request, *args, **kwargs):
        ''' List data with given id '''
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ''' Put or Update data '''
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ''' Delete data '''
        return self.destroy(request, *args, **kwargs)
