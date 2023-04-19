from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.vladelzi_zdani.models import TipVladelza
from apps.vladelzi_zdani.serializers import TipVladelzaSerializer

class TipVladelzaLV(APIView):
    def get(self, request, format=None):
        snippets = TipVladelza.objects.all()
        serializer = TipVladelzaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipVladelzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipVladelzaDV(APIView):

    def get_object(self, pk):
        try:
            return TipVladelza.objects.get(pk=pk)
        except TipVladelza.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        tip_vladelza = self.get_object(pk=id)
        serializer = TipVladelzaSerializer(tip_vladelza, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TipVladelzaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)