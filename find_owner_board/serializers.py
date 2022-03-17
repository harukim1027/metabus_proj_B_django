from rest_framework import serializers
from find_owner_board.models import FindOwnerBoard, FindOwnerBoardImage


class FindOwnerBoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoard
        fields = "__all__"


class FindOwnerBoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoardImage
        fields = "__all__"


class FindOwnerBoardSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    board_image = FindOwnerBoardImageSerializer(many=True, read_only=True)

    class Meta:
        model = FindOwnerBoard
        fields = ["find_board_no", "title", "content", "animal_type", "breed", "size",
                  "animal_tag", "find_location", "find_time", "board_image", "user", "created_at", "updated_at"]
