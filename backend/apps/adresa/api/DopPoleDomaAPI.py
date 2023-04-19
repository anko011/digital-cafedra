from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import DopPoleDoma
from apps.adresa.serializers.DopPoleDomaSerializer import DopPoleDomaSerializer


class DopPoleDomaLV(APIView):
    def get(self, request, format=None):
        snippets = DopPoleDoma.objects.all()
        serializer = DopPoleDomaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DopPoleDomaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DopPoleDomaDV(APIView):

    def get_object(self, pk):
        try:
            return DopPoleDoma.objects.get(pk=pk)
        except DopPoleDoma.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        dop_pole_doma = self.get_object(pk=id)
        serializer = DopPoleDomaSerializer(dop_pole_doma, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DopPoleDomaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)