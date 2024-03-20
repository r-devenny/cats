from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    NAMES_MAX_LENGTH = 50
    first_name = models.CharField(max_length=NAMES_MAX_LENGTH)
    last_name = models.CharField(max_length=NAMES_MAX_LENGTH)
    cats = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Students"


class Cat(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cats"