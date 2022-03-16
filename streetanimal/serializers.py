from rest_framework import serializers
from streetanimal.models import Animal


class AnimalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    date_of_discovery = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Animal
        fields = "__all__"
        depth = 1

