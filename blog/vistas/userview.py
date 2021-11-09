from django.contrib.auth.models import User
from django.http.response import Http404
from rest_framework.request import Request
from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.generalutilities.funciones import get_user_id
from blog.serializers.serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class User_APIView(APIView):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [permissions.IsAuthenticated]


        def get(self, request, format=None, *args, **kwargs):
                user = User.objects.all()
                serializer = UserSerializer(user,many = True, context = {'request':request})

                return Response(serializer.data)
        def post(self, request, format=None):
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User_APIView_detail(APIView):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [permissions.IsAuthenticated]

        
        def get(self,request, pk, format = None):
                user = get_user_id(pk)
                if user:
                        serialiazer = UserSerializer(user)
                        return Response(serialiazer.data)
        def delete (self, request, pk, format = None):
                user = get_user_id(pk)
                if user:
                        user.delete()
                        return Response(status=status.HTTP_204_NO_CONTENT)