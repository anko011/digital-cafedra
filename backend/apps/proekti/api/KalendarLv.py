from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.proekti.models import ResheniePoProektu


class KalendarLv(APIView):
    def get(self, request, format=None):

        result = []
        for reshenie in ResheniePoProektu.objects.filter(data_ispolnenia_po_resheniyu__isnull=False):
            result.append({
                'proekt_id':reshenie.proekt.id,
                'title':reshenie.get_calendar_title(),
                'start':reshenie.data_ispolnenia_po_resheniyu,
                'end':reshenie.data_ispolnenia_po_resheniyu,
            })

        return Response(result)



