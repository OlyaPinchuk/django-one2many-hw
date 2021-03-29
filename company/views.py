from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CompanyModel
from .serializers import CompanySerializer

# create POST
# read GET
# update PUT/PATCH
# delete DELETE


class ListCreateView(ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        qs = CompanyModel.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__iexact=name)
        return qs


class ReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

