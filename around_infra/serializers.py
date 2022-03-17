from rest_framework import serializers
from around_infra.models import AroundInfra


class AroundInfraCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AroundInfra
        fields = "__all__"

class AroundInfraSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = AroundInfra
        fields = "__all__"

