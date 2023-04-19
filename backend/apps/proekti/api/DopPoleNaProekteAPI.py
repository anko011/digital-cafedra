from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.proekti.models import DopPoleNaProekte
from apps.proekti.serializers import DopPoleNaProekteSerializer


class DopPoleNaProekteLV(APIView):
    def get(self, request, format=None):
        snippets = DopPoleNaProekte.objects.all()
        serializer = DopPoleNaProekteSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DopPoleNaProekteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DopPoleNaProekteDV(APIView):

    def get_object(self, pk):
        try:
            return DopPoleNaProekte.objects.get(pk=pk)
        except DopPoleNaProekte.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        dop_pole_na_proekte = self.get_object(pk=id)
        serializer = DopPoleNaProekteSerializer(dop_pole_na_proekte, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DopPoleNaProekteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)