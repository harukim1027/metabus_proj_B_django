from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from adopt_assignment.models import AdoptAssignment
from datetime import date


class AssignmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptAssignment
        fields = ["status"]


class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptAssignment
        fields = "__all__"

    def validate_date_to_meet(self, date_to_meet):
        if date_to_meet < date.today():
            raise ValidationError("지난 날짜는 예약할 수 없습니다.")
        return date_to_meet


class AssignmentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = AdoptAssignment
        fields = "__all__"
        depth = 2
