from django.contrib.auth.models import User
from rest_framework.relations import HyperlinkedIdentityField
from blog import models
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(view_name="blog:user-detail", read_only= True)
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partida
        fields = ['jugador','juego','duracion','puntos']
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'