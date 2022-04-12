from rest_framework import serializers
from lost_pet_board.models import LostPetBoard, LostPetBoardImage, LostPetBoardComment


class LostPetBoardImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoardImage
        fields = "__all__"


class LostPetBoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoardImage
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPetBoardComment
        fields = "__all__"
        depth = 1


class LostPetBoardSerializer(serializers.ModelSerializer):
    board_image = LostPetBoardImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    lost_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = LostPetBoard
        fields = "__all__"
        depth = 1


class LostPetBoardCreateSerializer(serializers.ModelSerializer):
    board_image = LostPetBoardImageSerializer(many=True, read_only=True)
    lost_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = LostPetBoard
        fields = ["lost_board_no", "title", "status", "content", "pet_name", "animal_type", "dog_breed", "cat_breed",
                  "sex", "animal_tag", "lost_location", "lost_time", "board_image", "user", "created_at", "updated_at"]

    def create(self, validated_data):
        images = self.context['request'].FILES.getlist('board_image')

        instance = LostPetBoard.objects.create(**validated_data)
        for image in images:
            LostPetBoardImage.objects.create(lost_board_no=instance, image=image)
        return instance

