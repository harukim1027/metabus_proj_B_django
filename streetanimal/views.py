from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q

from streetanimal.paginations.Pagination import AnimalPagination
from streetanimal.models import Animal, AllSecurityCenter
from streetanimal.serializers import AnimalSerializer, AnimalCreateSerializer, CenterSerializer


class AnimalPageViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    pagination_class = AnimalPagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AnimalSerializer
        return AnimalCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        kind = self.request.query_params.get("kind", "")
        sex = self.request.query_params.get("sex", "")
        breed = self.request.query_params.get("breed", "")
        place_of_discovery = self.request.query_params.get("place_of_discovery", "")

        if query:
            qs = qs.filter(announce_no__icontains=query)

        if kind:
            qs = qs.filter(kind_of_animal__exact=kind, sex__exact=sex, breed__exact=breed, place_of_discovery__icontains=place_of_discovery)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET" or method == "PATCH":
            return [AllowAny()]
        return [IsAuthenticated()]


class CentersViewSet(viewsets.ModelViewSet):
    queryset = AllSecurityCenter.objects.all()
    serializer_class = CenterSerializer


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
        kind = self.request.query_params.get("kind", "")
        sex = self.request.query_params.get("sex", "")
        breed = self.request.query_params.get("breed", "")
        place_of_discovery = self.request.query_params.get("place_of_discovery", "")

        if query:
            qs = qs.filter(announce_no__icontains=query)

        if kind:
            qs = qs.filter(kind_of_animal__exact=kind, sex__exact=sex, breed__exact=breed, place_of_discovery__icontains=place_of_discovery)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET" or method == "PATCH":
            return [AllowAny()]
        return [IsAuthenticated()]
