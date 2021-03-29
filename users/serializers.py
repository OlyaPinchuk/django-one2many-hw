from rest_framework.serializers import ModelSerializer
from company.serializers import CompanySerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    company = CompanySerializer(many=True, required=False)\


    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'company']
        extra_kwargs ={
            'password': {'write_only': True}
        }

    def create(self, validates_data):
        user = UserModel.objects.create_user(**validates_data)
        return user





