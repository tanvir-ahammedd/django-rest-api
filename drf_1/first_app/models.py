from django.db import models

# Create your models here.
class StudentData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    def __str__(self):
        return self.name

#one student can take multiple courses
#one to many
#many to one
#many -> course
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    #foreign key will be used at where many is placed
    student = models.ForeignKey(StudentData, on_delete=models.CASCADE, related_name='course')
    name = models.CharField(max_length=30)
    marks = models.IntegerField()
    def __str__(self):
        return f"{self.name}: {self.marks}"

    