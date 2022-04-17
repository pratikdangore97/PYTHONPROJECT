from django.db import models

# Create your models here.

class employee(models.Model):

    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=10)
    salary = models.IntegerField()
    is_active = models.CharField(max_length=1,default="Y")


    class Meta:

        db_table = "Employee"

    def __str__(self):
        return self.name
