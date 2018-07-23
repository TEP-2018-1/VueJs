from django.urls import path, include
from django.contrib import admin
from aplicacao import views

urlpatterns = [
    path('users/', views.UserList.as_view(),name=views.UserList.name),
    path('posts/',views.PostList.as_view(),name=views.PostList.name),
    path('posts/<int:pk>/', views.PostDetail.as_view(),name=views.PostDetail.name),
    path('users/<int:pk>/', views.UserDetail.as_view(),name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api-auth/', include('rest_framework.urls'))
]
