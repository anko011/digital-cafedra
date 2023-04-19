from rest_framework import serializers

from apps.adresa.models import Dom
from apps.proekti.models import ResheniePoProektu


class DomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dom
        fields = '__all__'


    proekti = serializers.SerializerMethodField()

    def get_proekti(self, obj):
        result = []
        for i in ResheniePoProektu.objects.filter(dom_id=obj.id):
            otvestveni = None
            tip_reshenia_po_proektu = None

            if i.tip_reshenia_po_proektu:
                tip_reshenia_po_proektu= i.tip_reshenia_po_proektu.nazvanie


            qr = i.proekt.uchastnikrabochaiagruppa_set.filter(is_otvestveni=True)
            if qr:
                otvestveni = qr.first().fio_uchastnika_gruppi
            result.append({

                'id':i.proekt_id,
                'vnutrinii_nomer':i.proekt.vnutrinii_nomer,
                'status':i.proekt.status_ispolnenia.nazvanie,
                'tip_reshenia_po_proektu':tip_reshenia_po_proektu,
                'data_ispolnenia_po_resheniyu':i.data_ispolnenia_po_resheniyu,
                'otvestveni':otvestveni,
            })

        return result

