from django.conf.urls import url, include
from .models import Object_folder
from rest_framework import routers, serializers, viewsets

# Сериализаторы описывают представление данных.
class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object_folder
        fields = ['name', 'name_films', 'name_cinema']

# Наборы представлений описывают поведение представлений.
class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object_folder.objects.all()
    serializer_class = ObjectSerializer


# Роутеры позволяют быстро и просто сконфигурировать адреса.
router = routers.DefaultRouter()
router.register(r'object', ObjectViewSet)

# Привяжите конфигурацию URL, используя роутеры.
# Так же мы предоставляем URL для авторизации в браузере.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]