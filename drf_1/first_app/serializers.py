from rest_framework import serializers
from . import models

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

#one student can take multiple courses -> one to many
class StudentSerializers(serializers.ModelSerializer):
    course = CourseSerializers(many = True, read_only=True)
    class Meta:
        model = models.StudentData
        fields = '__all__'