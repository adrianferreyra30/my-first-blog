from django.conf.urls import include, url
from django.urls import path
from blog import views
from blog.serializers.serializers import *
from rest_framework import routers
from blog.vistas import *
from blog.vistas.partidaview import Partida_APIView, Partida_APIView_Detail
from blog.vistas.postview import Post_APIView
from blog.vistas.userview import User_APIView, User_APIView_detail

app_name = 'blog'

urlpatterns = [
    url(r'users', User_APIView.as_view(), name='user-detail'),
    path('user/<int:pk>/', User_APIView_detail.as_view(),name='user-detail'),
    url(r'posts', Post_APIView.as_view()),
    url(r'partidas', Partida_APIView.as_view()),
    path('partida/<int:pk>/', Partida_APIView_Detail.as_view(),name='partida-detalle'),
    path('',Partida_APIView.as_view()),
    url(r'partida/new/', views.partida_new, name='partidas_new'),
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]