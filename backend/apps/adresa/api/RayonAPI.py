from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import Rayon
from apps.adresa.serializers import RayonSerializer


class RayonLV(APIView):
    def get(self, request, format=None):
        snippets = Rayon.objects.all()
        serializer = RayonSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RayonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RayonDV(APIView):

    def get_object(self, pk):
        try:
            return Rayon.objects.get(pk=pk)
        except Rayon.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        rayon = self.get_object(pk=id)
        serializer = RayonSerializer(rayon, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RayonSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)