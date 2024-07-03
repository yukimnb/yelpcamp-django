from campgrounds.models import Campground, Review
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.views import LoginView
from rest_framework import generics

# from rest_framework.permissions import IsAuthenticated ※あとで使う
from .serializers import CampgroundSerializer, ReviewSerializer


class CampgroundListCreateAPIView(generics.ListCreateAPIView):
    """キャンプ場の取得（一覧）・登録APIクラス"""

    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    # permission_classes = [IsAuthenticated]


class CampgroundRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """キャンプ場の取得（詳細）・更新・一部更新・削除APIクラス"""

    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = "id"


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    """コメントの取得（一覧）・登録APIクラス"""

    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(campground_id=self.kwargs["id"])


class ReviewDestroyAPIView(generics.DestroyAPIView):
    """コメントの削除APIクラス"""

    queryset = Review.objects.all()
    # permission_classes = [IsAuthenticated]
    lookup_field = "id"


class CustomLoginView(LoginView):
    """ログインAPIクラス"""

    serializer_class = LoginSerializer

    def get_response(self):
        response = super().get_response()
        response.data["id"] = self.user.id
        response.data["name"] = self.user.username
        return response
