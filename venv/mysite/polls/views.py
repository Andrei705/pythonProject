from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ObjectSerializer
from .models import Object_folder

class ObjectListView(APIView):

    def get(self,request):
        object = Object_folder.objects.filter()
        serializer = ObjectSerializer(object, many=True)
        return Response(serializer.data)
