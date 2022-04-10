from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from notice.models import Notice, NoticeImage, NoticeFile
from notice.paginations.Pagination import Pagination
from notice.serializers import NoticeSerializer, NoticeCreateSerializer, NoticeImageSerializer, \
    NoticeImageCreateSerializer, NoticeFileSerializer, NoticeFileCreateSerializer


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

    def create(self, request, *args, **kwargs):
        image_data = request.data.get("notice_image", None)
        file_data = request.data.get("notice_file", None)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        notice_no = serializer.data["notice_no"]
        image_serializer = NoticeImageSerializer(data={"image": image_data,
                                                               "notice_no": notice_no})
        file_serializer = NoticeFileSerializer(data={"file": file_data,
                                                               "notice_no": notice_no})

        if image_serializer.is_valid():
            image_serializer.save()

        if file_serializer.is_valid():
            file_serializer.save()

        return Response(serializer.data)


class NoticeImageViewSet(viewsets.ModelViewSet):
    queryset = NoticeImage.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return NoticeImageSerializer
        return NoticeImageCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class NoticeFileViewSet(viewsets.ModelViewSet):
    queryset = NoticeFile.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return NoticeFileSerializer
        return NoticeFileCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

