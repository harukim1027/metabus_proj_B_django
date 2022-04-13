from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from adopt_review.serializers import ReviewSerializer, ReviewCreateSerializer, CommentSerializer, ReviewImageSerializer, ReviewImageCreateSerializer, CommentCreateSerializer
from adopt_review.models import Review, AdoptReviewComment, AdoptReviewImage
from notice.paginations.Pagination import Pagination


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return ReviewSerializer
        return ReviewCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query) or qs.filter(review_no__icontains=query) or qs.filter(user__userID__icontains=query) or qs.filter(user__exact=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):

        image_data = request.data["review_image"]

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        review_no = serializer.data["review_no"]

        image_serializer = ReviewImageSerializer(data={"image": image_data,
                                                               "review_no": review_no})

        if image_serializer.is_valid():
            image_serializer.save()

        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = AdoptReviewComment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return CommentSerializer
        return CommentCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.query_params.get("query", "")

        if query:
            qs = qs.filter(user__exact=query)
        return qs


class ReviewAllViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return ReviewSerializer
        return ReviewCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(announce_no__icontains=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET" or method == "PATCH":
            return [AllowAny()]
        return [IsAuthenticated()]


class ReviewImageViewSet(viewsets.ModelViewSet):
    queryset = AdoptReviewImage.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return ReviewImageSerializer
        return ReviewImageCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
