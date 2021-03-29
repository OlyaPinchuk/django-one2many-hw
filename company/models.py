from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CompanyModel(models.Model):
    class Meta:
        db_table = 'companies'
        verbose_name = 'company'

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='company')