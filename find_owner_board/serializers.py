from rest_framework import serializers
from find_owner_board.models import FindOwnerBoard, FindOwnerBoardComment, FindOwnerBoardImage


class FindOwnerBoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoard
        fields = "__all__"


class FindOwnerBoardSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FindOwnerBoard
        fields = "__all__"


class FindOwnerBoardCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoardComment
        fields = "__all__"


class FindOwnerBoardCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FindOwnerBoardComment
        fields = "__all__"


class FindOwnerBoardImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoardImage
        fields = "__all__"


class FindOwnerBoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindOwnerBoardImage
        fields = "__all__"
