from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q

from notice.paginations.Pagination import Pagination
from streetanimal.models import Animal, AllSecurityCenter
from streetanimal.serializers import AnimalSerializer, AnimalCreateSerializer, CenterSerializer


class AnimalPageViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AnimalSerializer
        return AnimalCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(animal_no__icontains=query) or qs.filter(animal_reg_num__icontains=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET" or method == "PATCH":
            return [AllowAny()]
        return [IsAuthenticated()]


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AnimalSerializer
        return AnimalCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(animal_reg_num__icontains=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET" or method == "PATCH":
            return [AllowAny()]
        return [IsAuthenticated()]


class CentersViewSet(viewsets.ModelViewSet):
    queryset = AllSecurityCenter.objects.all()
    serializer_class = CenterSerializer

