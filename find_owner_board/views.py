from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from find_owner_board.models import FindOwnerBoard, FindOwnerBoardImage
from find_owner_board.serializers import FindOwnerBoardSerializer, FindOwnerBoardCreateSerializer
from find_owner_board.serializers import FindOwnerBoardImageSerializer, FindOwnerBoardImageCreateSerializer
from notice.paginations.Pagination import Pagination


class FindOwnerBoardViewSet(viewsets.ModelViewSet):
    queryset = FindOwnerBoard.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return FindOwnerBoardSerializer
        return FindOwnerBoardCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        location = self.request.query_params.get("location", "")
        if location:
            qs = qs.filter(find_location__icontains=location)

        animaltype = self.request.query_params.get("animaltype", "")
        if animaltype:
            qs = qs.filter(animal_type__icontains=animaltype)

        author = self.request.query_params.get("author", "")
        if author:
            qs = qs.filter(user__userID__icontains=author)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class FindOwnerBoardImageViewSet(viewsets.ModelViewSet):
    queryset = FindOwnerBoardImage.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return FindOwnerBoardImageSerializer
        return FindOwnerBoardImageCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
