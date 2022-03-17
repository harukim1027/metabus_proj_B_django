from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from around_infra.serializers import AroundInfraCreateSerializer, AroundInfraSerializer
from around_infra.models import AroundInfra
from notice.paginations.Pagination import Pagination


class AroundInfraViewSet(viewsets.ModelViewSet):
    queryset = AroundInfra.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AroundInfraSerializer
        return AroundInfraCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query) or qs.filter(inquiry_no__icontains=query) or qs.filter(user__userID__icontains=query)

        author = self.request.query_params.get("author", "")
        if author:
            qs = qs.filter(user__userID__exact=author)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
