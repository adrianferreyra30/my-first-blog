from django.contrib.auth.models import User
from django.http.response import Http404
from blog import models


def get_user_id(pk):
            try:
                    return User.objects.get(pk=pk)
            except User.DoesNotExist:
                    raise Http404
def get_object(pk):
        try:
            return models.Partida.objects.get(pk=pk)
        except models.Partida.DoesNotExist:
            raise Http404