from rest_framework import serializers
from notice.models import Notice, NoticeFile, NoticeImage


class NoticeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeImage
        fields = "__all__"


class NoticeImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeImage
        fields = "__all__"


class NoticeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeFile
        fields = "__all__"


class NoticeFileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeFile
        fields = "__all__"


class NoticeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    notice_image = NoticeImageSerializer(many=True, read_only=True)
    notice_file = NoticeFileSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = "__all__"
        depth = 1


class NoticeCreateSerializer(serializers.ModelSerializer):
    notice_image = NoticeImageSerializer(many=True, read_only=True)
    notice_file = NoticeFileSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ["notice_no", "title", "content", "user", "notice_image", "notice_file", "created_at", "updated_at"]

    def create(self, validated_data):
        images = self.context['request'].FILES.getlist('notice_image')
        files = self.context['request'].FILES.getlist('notice_file')

        instance = Notice.objects.create(**validated_data)
        for image in images:
            NoticeImage.objects.create(notice_no=instance, image=image)

        for file in files:
            NoticeFile.objects.create(notice_no=instance, file=file, filename=file.name)
        return instance
