from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.proekti.models import ResheniePoProektu
from apps.proekti.serializers import ResheniePoProektuSerializer


class ResheniePoProektuLV(APIView):
    def get(self, request, format=None):
        snippets = ResheniePoProektu.objects.all()
        serializer = ResheniePoProektuSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ResheniePoProektuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResheniePoProektuDV(APIView):

    def get_object(self, pk):
        try:
            return ResheniePoProektu.objects.get(pk=pk)
        except ResheniePoProektu.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        reshenie_po_proektu = self.get_object(pk=id)
        serializer = ResheniePoProektuSerializer(reshenie_po_proektu, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ResheniePoProektuSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)