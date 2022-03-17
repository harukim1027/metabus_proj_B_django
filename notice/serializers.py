from rest_framework import serializers
from notice.models import Notice, NoticeFile, NoticeImage


class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"


class NoticeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeImage
        fields = "__all__"


class NoticeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeFile
        fields = "__all__"


class NoticeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    notice_image = NoticeImageSerializer(read_only=True)
    notice_file = NoticeFileSerializer(read_only=True)

    class Meta:
        model = Notice
        fields = "__all__"
        depth = 1


