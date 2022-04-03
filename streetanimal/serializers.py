from rest_framework import serializers
from streetanimal.models import Animal, AllSecurityCenter


class AnimalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"



class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllSecurityCenter
        fields = "__all__"


# 데이트 타임 필드 삭제
class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = "__all__"
        depth = 1


