from rest_framework import serializers
from streetanimal.models import Animal, AnimalImage


class AnimalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalImage
        fields = "__all__"



class AnimalSerializer(serializers.ModelSerializer):
    date_time_of_receipt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    period_of_announcement = serializers.DateField(format="%Y-%m-%d")

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    announce_image = AnimalImageSerializer(many=True, read_only=True)

    class Meta:
        model = Animal
        fields = "__all__"
        depth = 1


