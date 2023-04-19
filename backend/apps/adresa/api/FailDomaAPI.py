from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import FailDoma
from apps.adresa.serializers import FailDomaSerializer


class FailDomaLV(APIView):
    def get(self, request, format=None):
        snippets = FailDoma.objects.all()
        serializer = FailDomaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FailDomaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FailDomaDV(APIView):

    def get_object(self, pk):
        try:
            return FailDoma.objects.get(pk=pk)
        except FailDoma.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        faili_doma = self.get_object(pk=id)
        serializer = FailDomaSerializer(faili_doma, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FailDomaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)