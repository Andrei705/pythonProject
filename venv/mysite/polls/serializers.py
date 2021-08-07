from rest_framework import serializers
from .models import Object_folder


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object_folder
        fields = ['id', 'name', 'name_films', 'name_cinema']