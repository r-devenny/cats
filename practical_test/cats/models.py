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

    def save(self, *args, **kwargs):
        # If this is a new cat, increment the cat count for the student
        if not self.pk:
            self.student.cats += 1
            self.student.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Decrement the cat count for the student when a cat is deleted
        self.student.cats -= 1
        self.student.save()
        super().delete(*args, **kwargs)