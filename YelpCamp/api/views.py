from campgrounds.models import Campground
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import CampgroundSerializer, CustomUserSerializer


class CampgroundListCreateAPIView(generics.ListCreateAPIView):
    """キャンプ場の取得（一覧）・登録APIクラス"""

    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    permission_classes = [IsAuthenticated]


class CampgroundRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """キャンプ場の取得（詳細）・更新・一部更新・削除APIクラス"""

    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class CustomUserCreateAPIView(generics.CreateAPIView):
    """ユーザーの登録APIクラス"""

    serializer_class = CustomUserSerializer
