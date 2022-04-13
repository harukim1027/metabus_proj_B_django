from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from find_owner_board.models import FindOwnerBoard, FindOwnerBoardImage, FindOwnerBoardComment
from find_owner_board.serializers import FindOwnerBoardSerializer, FindOwnerBoardCreateSerializer, CommentSerializer, \
    CommentCreateSerializer
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

        status = self.request.query_params.get("status", "")
        if status:
            qs = qs.filter(status__icontains=status)

        author = self.request.query_params.get("author", "")
        if author:
            qs = qs.filter(user__userID__icontains=author)

        query = self.request.query_params.get("query", "")

        if query:
            qs = qs.filter(user__exact=query)

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

        find_board_no = serializer.data["find_board_no"]

        image_serializer = FindOwnerBoardImageSerializer(data={"image": image_data,
                                                               "find_board_no": find_board_no})

        if image_serializer.is_valid():
            image_serializer.save()

        return Response(serializer.data)


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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = FindOwnerBoardComment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return CommentSerializer
        return CommentCreateSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.query_params.get("query", "")

        if query:
            qs = qs.filter(user__exact=query)
        return qs