from rest_framework import viewsets

from .serializers import ObjectSerializer
from .models import Object_folder

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object_folder.objects.all().order_by('name')
    serializer_class = ObjectSerializer