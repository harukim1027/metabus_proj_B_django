from rest_framework import serializers
from adopt_review.models import Review, AdoptReviewImage


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptReviewImage
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    Review_image = ReviewImageSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
        depth = 2

