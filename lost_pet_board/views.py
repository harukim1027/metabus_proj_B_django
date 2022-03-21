from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from lost_pet_board.models import LostPetBoard, LostPetBoardImage
from lost_pet_board.serializers import LostPetBoardSerializer, LostPetBoardCreateSerializer
from lost_pet_board.serializers import LostPetBoardImageSerializer, LostPetBoardImageCreateSerializer


class LostPetViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoard.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return LostPetBoardSerializer
        return LostPetBoardCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class LostPetBoardImageViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoardImage.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return LostPetBoardImageSerializer
        return LostPetBoardImageCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
