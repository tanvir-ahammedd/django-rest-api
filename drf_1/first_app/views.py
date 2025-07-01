from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

class StudentView(APIView):
    def get(self, request, format=None):
        student = models.StudentData.objects.all()
        serializer =serializers.StudentSerializers(student, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = serializers.StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
 
class StudentDetailView(APIView):

    def get_object(self, pk):
        # This method fetches a student by primary key or raises a 404
        return get_object_or_404(models.StudentData, pk=pk)

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = serializers.StudentSerializers(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = serializers.StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)