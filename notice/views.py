from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from notice.models import Notice
from notice.paginations.Pagination import Pagination
from notice.serializers import NoticeSerializer, NoticeCreateSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return NoticeSerializer
        return NoticeCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query) or qs.filter(notice_no__icontains=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
