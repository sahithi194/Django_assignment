from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=255)
    id =models.AutoField(primary_key=True)
    course=models.CharField(max_length=255)
    city =models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.name} {self.course} {self.city}'