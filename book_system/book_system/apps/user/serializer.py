from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django_redis import get_redis_connection
from .models import *
import re


class LoginTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)

        refresh = self.get_token(self.user)

        data["token"] = str(refresh)
        data["username"] = self.user.username
        data["avatar"] = self.user.avatar
        return {
            "code": 200,
            "msg": "ok",
            "data": data
        }


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    需要校验的字段 ['username', 'password', 'password1', 'email']
    序列化字段 ['id', 'username', 'avatar']
    反序列化字段 ['username', 'password', 'password1', 'email']
    模型中不存在的字段 ['password1']
    """
    password1 = serializers.CharField(label='password2', write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'gender', 'password', 'password1', 'email', 'avatar']
        extra_kwargs = {
            'username': {
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '用户名最小长度不能小于6',
                    'max_length': '用户名最大长度不能大于20',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '密码最小长度不能小于8',
                    'max_length': '密码最大长度不能大于20',
                }
            },
            'avatar': {
                'default': 'https://up.enterdesk.com/edpic_source/01/4a/d1/014ad16ceb77e3563cfe41fbc59333e4.jpg'
            }

        }

    def validated_email(self, value: str):
        """
        check email format
        :return:
        """
        if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', value):
            raise serializers.ValidationError('error for email format')
        return value



    def validate(self, attrs):
        """
        校验两次密码是否一致
        校验手机验证码是否正确

        :param attrs:
        :return:
        """
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError('两次密码不一致，请重写输入密码')
        return attrs

    def create(self, validated_data):
        del validated_data['password1']
        #password = validated_data.pop("password")
        #user = User(**validated_data)
        user = super().create(validated_data)
        # 将密码加密并赋值
        user.set_password(validated_data['password'])
        user.save()
        print (user.password)
        return user