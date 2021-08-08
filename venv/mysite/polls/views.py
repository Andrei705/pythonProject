from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ObjectSerializer
from .models import Object_folder

class ObjectListView(APIView):

    def get(self,request, id=1):
        object = Object_folder.objects.filter()
        serializer = ObjectSerializer(object, many=True)
        return Response(serializer.data)
