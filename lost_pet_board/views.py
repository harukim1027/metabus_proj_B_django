from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from lost_pet_board.models import LostPetBoard, LostPetBoardImage, LostPetBoardComment
from lost_pet_board.serializers import LostPetBoardSerializer, LostPetBoardCreateSerializer, CommentSerializer
from lost_pet_board.serializers import LostPetBoardImageSerializer, LostPetBoardImageCreateSerializer
from notice.paginations.Pagination import Pagination


class LostPetViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoard.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return LostPetBoardSerializer
        return LostPetBoardCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        location = self.request.query_params.get("location", "")
        if location:
            qs = qs.filter(lost_location__icontains=location)

        animaltype = self.request.query_params.get("animaltype", "")
        if animaltype:
            qs = qs.filter(animal_type__icontains=animaltype)

        status = self.request.query_params.get("status", "")
        if status:
            qs = qs.filter(status__icontains=status)

        author = self.request.query_params.get("author", "")
        if author:
            qs = qs.filter(user__userID__icontains=author)

        sex = self.request.query_params.get("sex", "")
        if sex:
            qs = qs.filter(sex__icontains=sex)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):

        image_data = request.data["board_image"]

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        lost_board_no = serializer.data["lost_board_no"]

        image_serializer = LostPetBoardImageSerializer(data={"image": image_data,
                                                             "lost_board_no": lost_board_no})

        if image_serializer.is_valid():
            image_serializer.save()

        return Response(serializer.data)


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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoardComment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = Pagination
