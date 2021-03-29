from django.urls import path
from .views import ListCreateEmployeeView

urlpatterns = [
    path('', ListCreateEmployeeView.as_view())
]