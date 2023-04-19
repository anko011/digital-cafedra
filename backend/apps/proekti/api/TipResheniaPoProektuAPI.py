from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.proekti.models import TipResheniaPoProektu
from apps.proekti.serializers import TipResheniaPoProektuSerializer


class TipResheniaPoProektuLV(APIView):
    def get(self, request, format=None):
        snippets = TipResheniaPoProektu.objects.all()
        serializer = TipResheniaPoProektuSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipResheniaPoProektuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipResheniaPoProektuDV(APIView):

    def get_object(self, pk):
        try:
            return TipResheniaPoProektu.objects.get(pk=pk)
        except TipResheniaPoProektu.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        tip_reshenia_po_proektu = self.get_object(pk=id)
        serializer = TipResheniaPoProektuSerializer(tip_reshenia_po_proektu, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TipResheniaPoProektuSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)