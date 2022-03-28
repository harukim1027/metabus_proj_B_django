from rest_framework import serializers
from find_owner_board.models import FindOwnerBoard, FindOwnerBoardImage


class FindOwnerBoardImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoardImage
        fields = "__all__"


class FindOwnerBoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoardImage
        fields = "__all__"


class FindOwnerBoardSerializer(serializers.ModelSerializer):
    board_image = FindOwnerBoardImageSerializer(many=True, read_only=True)

    class Meta:
        model = FindOwnerBoard
        fields = "__all__"


class FindOwnerBoardCreateSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    board_image = FindOwnerBoardImageSerializer(many=True, read_only=True)
    # 기본적으로 중첩된 Serializer 에서는 쓰기(Create), 갱신(Update)를 지원해주지 않음. 그래서 read_only=True 옵션을 넣음

    class Meta:
        model = FindOwnerBoard
        fields = ["find_board_no", "title", "status", "content", "animal_type", "dog_breed", "cat_breed", "size", "sex",
                  "animal_tag", "find_location", "find_time", "board_image", "user", "created_at", "updated_at"]

    def create(self, validated_data):
        images = self.context['request'].FILES.getlist('board_image')

        instance = FindOwnerBoard.objects.create(**validated_data)
        for image in images:
            FindOwnerBoardImage.objects.create(find_board_no=instance, image=image)
        return instance

