from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from lost_pet_board.models import LostPetBoard
from lost_pet_board.serializers import LostPetBoardSerializer, LostPetBoardCreateSerializer


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


