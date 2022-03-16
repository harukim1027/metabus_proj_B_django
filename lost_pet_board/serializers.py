from rest_framework import serializers
from lost_pet_board.models import LostPetBoard


class LostPetBoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoard
        fields = "__all__"


class LostPetBoardSerializer(serializers.ModelSerializer):
    lost_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = LostPetBoard
        fields = "__all__"

