from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q
from rest_framework.response import Response

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
        centerid = self.request.query_params.get("centerid", "")

        if query:
            qs = qs.filter(announce_no__icontains=query)

        if kind:
            qs = qs.filter(kind_of_animal__exact=kind, sex__exact=sex, breed__exact=breed, place_of_discovery__icontains=place_of_discovery)

        if centerid:
            qs = qs.filter(center_name__center_name__exact=centerid)

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
        center_name = self.request.query_params.get("center_name", "")

        if query:
            qs = qs.filter(announce_no__icontains=query)

        if kind:
            qs = qs.filter(kind_of_animal__exact=kind, sex__exact=sex, breed__exact=breed)

        if center_name:
            qs = qs.filter(center_name__exact=center_name)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET" or method == "PATCH":
            return [AllowAny()]
        return [IsAuthenticated()]


@api_view()
def stat(request):
    return Response({
        "count": Animal.objects.filter(protect_status='보호중').count(),
        "process": Animal.objects.filter(protect_status='입양 매칭 중').count(),
        "complite": Animal.objects.filter(protect_status='입양 완료').count(),
    })

