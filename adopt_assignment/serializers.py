from rest_framework import serializers
from adopt_assignment.models import AdoptAssignment, AdoptAssignmentHomeImage


class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptAssignment
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateField(format="%Y-%m-%d")
    home_image = AssignmentImageSerializer(many=True, read_only=True)

    class Meta:
        model = AdoptAssignment
        fields = "__all__"
        depth = 2
