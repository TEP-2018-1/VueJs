
from rest_framework import serializers
from .models import *


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="name")
    class Meta:
        model = Post
        fields = ("url", "id", "title", "body", "user")

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),
                                        slug_field="name")
    class Meta:
         model = Post
         fields = ("url", "title", "body", "user")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "id", "name", "email")


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "name", "email", "posts")
