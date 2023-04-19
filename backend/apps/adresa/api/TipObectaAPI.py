from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import TipObecta
from apps.adresa.serializers import TipObectaSerializer


class TipObectaLV(APIView):
    def get(self, request, format=None):
        snippets = TipObecta.objects.all()
        serializer = TipObectaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipObectaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipObectaDV(APIView):

    def get_object(self, pk):
        try:
            return TipObecta.objects.get(pk=pk)
        except TipObecta.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        tip_obecta = self.get_object(pk=id)
        serializer = TipObectaSerializer(tip_obecta, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TipObectaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)