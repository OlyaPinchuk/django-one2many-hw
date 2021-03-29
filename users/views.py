from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

UserModel = get_user_model()


class ListCreateUserView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
