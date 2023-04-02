from django.http.response import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginTokenSerializer, UserRegisterSerializer

from .models import User


class LoginTokenView(TokenObtainPairView):
    """
    登录获取token接口
    """

    serializer_class = LoginTokenSerializer
    permission_classes = []


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class UsernameCountView(APIView):
    """判断用户名是否重复注册"""

    def get(self, request, username):
        """
        :param request: 请求对象
        :param username: 用户名
        :return: JSON
        """
        count = User.objects.filter(username=username).count()
        return Response({'code': status.HTTP_200_OK, 'msg': 'OK', 'count': count})


class EmailCountView(APIView):
    """判断用户名是否重复注册"""

    def get(self, request, email):
        """
        :param request: 请求对象
        :param email: email
        :return: JSON
        """
        count = User.objects.filter(email=email).count()
        return Response({'code': status.HTTP_200_OK, 'msg': 'OK', 'count': count})