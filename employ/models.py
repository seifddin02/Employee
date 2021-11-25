from django.db import models

# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=250, null=True)

    DEPARTMENT = (
        ('IT', 'IT'),
        ('Accounting', 'Accounting'),
        ('Management', 'Management'),
        ('HR', 'HR'),
        ('Marketing', 'Marketing'),
        ('finance', 'finance'),
    )

    department = models.CharField(max_length=250, null=True, choices=DEPARTMENT)
    address = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    employment_date = models.CharField(max_length=10, null=True)
    birth_date = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name