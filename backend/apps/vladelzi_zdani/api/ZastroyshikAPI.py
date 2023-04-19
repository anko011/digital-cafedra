from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.vladelzi_zdani.models import Zastroyshik
from apps.vladelzi_zdani.serializers import ZastroyshikSerializer


class ZastroyshikLV(APIView):
    def get(self, request, format=None):
        snippets = Zastroyshik.objects.all()
        serializer = ZastroyshikSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ZastroyshikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZastroyshikDV(APIView):

    def get_object(self, pk):
        try:
            return Zastroyshik.objects.get(pk=pk)
        except Zastroyshik.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        zastroyshik = self.get_object(pk=id)
        serializer = ZastroyshikSerializer(zastroyshik, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ZastroyshikSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)