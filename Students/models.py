from django.db import models


# class SampleTable(models.Model):

#     age = models.IntegerField(default=10)
#     weight = models.FloatField(null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     name = models.CharField(max_length=150)
#     feedback = models.TextField()

#     date_of_birth = models.DateField(auto_now=True)
#     date_of_birth_with_time = models.DateTimeField()
#     birth_time = models.TimeField()

#     is_admin = models.BooleanField()

class Student(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):

        return self.name


class Task(models.Model):

    task_name = models.CharField(max_length=200)
    description = models.TextField()