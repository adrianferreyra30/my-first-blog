from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from blog import models
from blog.generalutilities.funciones import get_object
from blog.serializers.serializers import PartidaSerializer


class Partida_APIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog\partidas_list.html'

    def get(self,request):
        partida = models.Partida.objects.all()
        return Response({'partidas': partida})
    def post(self, request, format=None):
        serializer = PartidaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Partida_APIView_Detail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
            
    def get(self, request, pk, format=None):
        partida = get_object(pk)
        if partida:
            serializer = PartidaSerializer(partida)  
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk, format=None):
        partida = get_object(pk)
        serializer = PartidaSerializer(partida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        partida = get_object(pk)
        if partida:
            partida.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)