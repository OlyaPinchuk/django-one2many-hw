from django.db import models
from company.models import CompanyModel


class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employee'
        verbose_name = 'employee'

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='employee')
