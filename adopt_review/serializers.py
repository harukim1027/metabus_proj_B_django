from rest_framework import serializers
from adopt_review.models import Review, AdoptReviewImage, AdoptReviewComment


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptReviewImage
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptReviewComment
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    review_image = ReviewImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ["review_no", "title", "content", "user", "adoptassignment", "created_at",
                  "updated_at", "review_image", "comments"]
        depth = 2

