from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from adopt_review.serializers import ReviewSerializer, ReviewCreateSerializer
from adopt_review.models import Review
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
            qs = qs.filter(title__icontains=query) or qs.filter(review_no__icontains=query) or qs.filter(user__userID__icontains=query)

        category = self.request.query_params.get("category", "")
        if category:
            qs = qs.filter(adoptassignment__animal__category__name__exact=category)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
