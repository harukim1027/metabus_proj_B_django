from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from find_owner_board.models import FindOwnerBoard
from find_owner_board.serializers import FindOwnerBoardSerializer, FindOwnerBoardCreateSerializer


class FindOwnerBoardViewSet(viewsets.ModelViewSet):
    queryset = FindOwnerBoard.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return FindOwnerBoardSerializer
        return FindOwnerBoardCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
