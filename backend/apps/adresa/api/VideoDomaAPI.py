from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import VideoDoma
from apps.adresa.serializers.VideoDomaSerializer import VideoDomaSerializer


class VideoDomaLV(APIView):
    def get(self, request, format=None):
        snippets = VideoDoma.objects.all()
        serializer = VideoDomaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VideoDomaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoDomaDV(APIView):

    def get_object(self, pk):
        try:
            return VideoDoma.objects.get(pk=pk)
        except VideoDoma.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        video_doma = self.get_object(pk=id)
        serializer = VideoDomaSerializer(video_doma, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VideoDomaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)