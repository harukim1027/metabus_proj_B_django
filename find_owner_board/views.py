from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

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

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    #################################################################

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()

    ######################################################################
    def create(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        board_data = request.data
        image_data = board_data
        print(image_data)
        serializer = self.get_serializer(data=board_data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        image_serializer = FindOwnerBoardImageSerializer.objects.create(image=image_data, find_board_no=serializer.data.find_board_no)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    # def perform_create(self, serializer):
    #     super().perform_create(serializer)


    # def create(self,validated_data):
        # 있으면 업데이트 없으면 생성
        # result, created = FileList.objects.get_or_create(
        #     name=board_image,

        # )

        # serializer = self.get_serializer(data=request.data)
        # self.perform_create(serializer)
        # board_images = self.request['request'].FILES
        # findownerboard = FindOwnerBoard.objects.create(**validated_data)
        # for board_image in board_images.getlist('image'):
        #     FindOwnerBoardImage.objects.create(findownerboard=findownerboard, image=board_image)
        # return findownerboard

    # 이미지 저장을 위해 추가
    # def create(self, serializer):
    #     serializer.save(find_board_no=self.request.user)

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
