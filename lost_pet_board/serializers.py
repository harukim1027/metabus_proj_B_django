from rest_framework import serializers
from lost_pet_board.models import LostPetBoard, LostPetBoardImage


class LostPetBoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoard
        fields = "__all__"


class LostPetBoardImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoardImage
        fields = "__all__"


class LostPetBoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoardImage
        fields = "__all__"


class LostPetBoardSerializer(serializers.ModelSerializer):
    # lost_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    board_image = LostPetBoardImageSerializer(many=True, read_only=True)

    class Meta:
        model = LostPetBoard
        fields = ["lost_board_no", "title", "status", "content", "pet_name", "animal_type", "dog_breed", "cat_breed", "size",
                  "sex", "animal_tag", "lost_location", "lost_time", "board_image", "user", "created_at", "updated_at"]

    def create(self, validated_data):
        images = self.context['request'].FILES.getlist('board_image')

        instance = LostPetBoard.objects.create(**validated_data)
        for image in images:
            LostPetBoardImage.objects.create(find_board_no=instance, image=image)
        return instance
