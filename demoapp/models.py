from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.CharField(max_length=250)



class Student(models.Model):
    name=models.CharField(max_length=250)
    roll_no=models.IntegerField()
    mark=models.IntegerField()


class Employee(models.Model):
    name=models.CharField(max_length=250)
    dept=models.CharField(max_length=250)
    salary=models.IntegerField()


class College(models.Model):
    name=models.CharField(max_length=250)
    place=models.CharField(max_length=250)
    phno=models.IntegerField()













