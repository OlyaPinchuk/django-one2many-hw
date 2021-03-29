from django.urls import path, include

urlpatterns = [
    path('/companies', include('company.urls')),
    path('/employees', include('employee.urls')),
    path('/users', include('users.urls'))
]