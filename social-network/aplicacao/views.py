from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from rest_framework import generics
import json


# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    name = 'post-detail'

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    name = 'user-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
                         'posts': reverse(PostList.name, request=request),

                         'users': reverse(UserList.name, request=request)
                         })



def ImportaDB():
    # json_data = json.load(open('db.json').read())

    # dump_data = open('db.json', 'r')
    # as_json = json.load(dump_data)
    #
    # for user in as_json['users']:
    #     geo = Geo.objects.create(lat=user['address']['geo']['lat'],
    #                              lng=user['address']['geo']['lng'])
    #     address = Address.objects.create(street=user['address']['street'],
    #                                      suite=user['address']['suite'],
    #                                      city=user['address']['city'],
    #                                      zipcode=user['address']['zipcode'],
    #                                      geo=geo)
    #     user = User.objects.create(username=user['username'],
    #                                 email=user['email'])
    #     Pessoa.objects.create(
    #                         name=user['name'],
    #                         email=user['email'],
    #                         address=address,
    #                         user = user)
    #
    #
    # for post in as_json['posts']:
    #     user = User.objects.get(id=post['userId'])
    #     Post.objects.create(id=post['id'],
    #                         title=post['title'],
    #                         body=post['body'],
    #                         user=user)
    #
    # for comment in as_json['comments']:
    #     post = Post.objects.get(id=comment['postId'])
    #     Comment.objects.create(id=comment['id'],
    #                            name=comment['name'],
    #                            email=comment['email'],
    #                            body=comment['body'],
    #                            post=post)

        dump_data = open('db.json', 'r')
        as_json = json.load(dump_data)
        for user in as_json['users']:
            geo = Geo.objects.create(lat=user['address']['geo']['lat'],
                                     lng=user['address']['geo']['lng'])
            address = Address.objects.create(street=user['address']['street'],
                                             suite=user['address']['suite'],
                                             city=user['address']['city'],
                                             zipcode=user['address']['zipcode'],
                                             geo=geo)
            
            user = User(id=user['id'],
                               name=user['name'],
                               email=user['email'],
                               
                               address=address)
            user.save()


        for post in as_json['posts']:
            usuario = User.objects.get(id=post['userId'])

            Post.objects.create(id=post['id'],
                                title=post['title'],
                                body=post['body'],
                                user=usuario)

        for comment in as_json['comments']:
            post = Post.objects.get(id=comment['postId'])
            Comment.objects.create(id=comment['id'],
                                   name=comment['name'],
                                   email=comment['email'],
                                   body=comment['body'],
                                   post=post)
