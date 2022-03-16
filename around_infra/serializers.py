from rest_framework import serializers
from around_infra.models import AroundInfra


class AroundInfraCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AroundInfra
        fields = "__all__"
