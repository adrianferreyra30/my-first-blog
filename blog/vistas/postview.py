from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from blog import models
from blog.serializers.serializers import PostSerializer


class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = models.Post.objects.all()
        serializer = PostSerializer(post,many = True)

        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)