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

        # def get_images(self, obj):
        #     image = obj.FindOwnerBoardImage_set.all()
        #     return FindOwnerBoardImageSerializer(instance=image, many=True).data

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

    # # 추가
    # def create(self, validated_data):
    #     image_data = validated_data.pop('findownerboardimage')
    #     findownerboard = FindOwnerBoard.objects.create(**validated_data)
    #
    #     for findownerboardimage in image_data:
    #         FindOwnerBoardImage.objects.create(findownerboard=findownerboard, **findownerboardimage)
    #     return findownerboard


    # board_image 도 한번에 저장하기 위한 함수
    # def create(self, validated_data):
    #     instance = FindOwnerBoard.objects.create(**validated_data)
    #     image_set = self.context['request'].FILES
    #     for image_data in image_set.getlist('image'):
    #         FindOwnerBoardImage.objects.create(FindOwnerBoard=instance, image=image_data)
    #     return instance
    #
    #     board_images = self.context['request'].FILES
    #     findownerboard = FindOwnerBoard.objects.create(**validated_data)
    #     for board_image in board_images.getlist('image'):
    #         FindOwnerBoardImage.objects.create(findownerboard=findownerboard, image=board_image)
    #     return findownerboard
