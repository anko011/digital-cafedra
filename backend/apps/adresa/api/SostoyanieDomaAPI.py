from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import SostoyanieDoma
from apps.adresa.serializers import SostoyanieDomaSerializer

class SostoyanieDomaLV(APIView):
    def get(self, request, format=None):
        snippets = SostoyanieDoma.objects.all()
        serializer = SostoyanieDomaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SostoyanieDomaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SostoyanieDomaDV(APIView):

    def get_object(self, pk):
        try:
            return SostoyanieDoma.objects.get(pk=pk)
        except SostoyanieDoma.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        sostoyanie_doma = self.get_object(pk=id)
        serializer = SostoyanieDomaSerializer(sostoyanie_doma, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SostoyanieDomaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)