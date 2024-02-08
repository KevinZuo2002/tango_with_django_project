from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    views = models.IntegerField(default=0)

class Department(models.Model):
    department_name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=128)

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=128)
    employee_number = models.CharField(max_length=128)
