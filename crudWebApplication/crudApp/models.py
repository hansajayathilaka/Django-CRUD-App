from django.db import models


class Employee(models.Model):
    eId = models.CharField(max_length=20)
    eName = models.CharField(max_length=100)
    eEmail = models.EmailField()
    eContact = models.CharField(max_length=15)

    class Meta:
        db_table = 'employee'
