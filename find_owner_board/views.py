from django.shortcuts import render
from rest_framework import viewsets
from find_owner_board.serializers import FindOwnerBoardSerializer, FindOwnerBoardCreateSerializer
from find_owner_board.serializers import FindOwnerBoardCommentSerializer, FindOwnerBoardCommentCreateSerializer
from find_owner_board.serializers import FindOwnerBoardImageSerializer, FindOwnerBoardImageCreateSerializer
from find_owner_board.models import FindOwnerBoard, FindOwnerBoardComment, FindOwnerBoardImage


class FindOwnerBoardViewSet(viewsets.ModelViewSet):
    queryset = FindOwnerBoard.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return FindOwnerBoardSerializer
        return FindOwnerBoardCreateSerializer


class FindOwnerBoardCommentViewSet(viewsets.ModelViewSet):
    queryset = FindOwnerBoardComment.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return FindOwnerBoardCommentSerializer
        return FindOwnerBoardCommentCreateSerializer


class FindOwnerBoardImageViewSet(viewsets.ModelViewSet):
    queryset = FindOwnerBoardImage.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return FindOwnerBoardImageSerializer
        return FindOwnerBoardImageCreateSerializer

