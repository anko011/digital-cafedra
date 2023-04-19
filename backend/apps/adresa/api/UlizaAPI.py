from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import Uliza
from apps.adresa.serializers.UlizaSerializer import UlizaSerializer


class UlizaLV(APIView):
    def get(self, request, format=None):
        snippets = Uliza.objects.all()
        serializer = UlizaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UlizaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UlizaDV(APIView):

    def get_object(self, pk):
        try:
            return Uliza.objects.get(pk=pk)
        except Uliza.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        uliza = self.get_object(pk=id)
        serializer = UlizaSerializer(uliza, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UlizaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)