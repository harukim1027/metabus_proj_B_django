from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from adopt_assignment.models import AdoptAssignment
from adopt_assignment.serializers import AssignmentSerializer, AssignmentCreateSerializer, AssignmentStatusSerializer
from notice.paginations.Pagination import Pagination


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = AdoptAssignment.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AssignmentSerializer
        elif method == "PATCH":
            return AssignmentStatusSerializer
        return AssignmentCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        author = self.request.query_params.get("author", "")

        if query:
            qs = qs.filter(assignment_no__icontains=query) or qs.filter(adopter_name__icontains=query) or qs.filter(animal__announce_no__icontains=query) or qs.filter(user__nickname__icontains=query)

        if author:
            qs = qs.filter(user__userID__exact=author)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]



class AssignmentPagingViewSet(viewsets.ModelViewSet):
    queryset = AdoptAssignment.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AssignmentSerializer
        return AssignmentCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        author = self.request.query_params.get("author", "")

        if query:
            qs = qs.filter(assignment_no__icontains=query) or qs.filter(adopter_name__icontains=query) or qs.filter(animal__announce_no__icontains=query) or qs.filter(user__nickname__icontains=query)

        if author:
            qs = qs.filter(user__userID__exact=author)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
