from rest_framework import serializers

from apps.proekti.models import Proekt


class ProektSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proekt
        fields = [
            'id',
            'vnutrinii_nomer',
            'status',
            'raioni',
            'blizaishaia_data',
            'otvestvenie',
            'doma'
        ]

    status = serializers.SerializerMethodField()
    raioni = serializers.SerializerMethodField()
    blizaishaia_data = serializers.SerializerMethodField()
    otvestvenie = serializers.SerializerMethodField()
    doma = serializers.SerializerMethodField()

    def get_status(self, obj):
        if obj.status_ispolnenia:
            return obj.status_ispolnenia.nazvanie

    def get_raioni(self, obj):
        doma_po_proektu = obj.resheniepoproektu_set.all()
        spisok_raionov = []
        for i in doma_po_proektu:
            raion = i.dom.get_rayon()
            if raion:
                spisok_raionov.append(raion.name)
        return set(spisok_raionov)

    def get_otvestvenie(self, obj):
        spisok_otvestvennih = []
        for i in obj.uchastnikrabochaiagruppa_set.filter(is_otvestveni=True):
            spisok_otvestvennih.append(i.fio_uchastnika_gruppi)
        return spisok_otvestvennih

    def get_blizaishaia_data(self, obj):
        try:
            return obj.resheniepoproektu_set.all() \
                .order_by('data_ispolnenia_po_resheniyu') \
                .first() \
                .data_ispolnenia_po_resheniyu
        except Exception:
            return '-'

    def get_doma(self, obj):
        result = []
        for i in obj.resheniepoproektu_set.all():
            result.append({
                'adres': i.dom.get_full_adres(),
                'ploshad': i.dom.ploshad,
                'tip_obekta': i.dom.tip_obecta.name if i.dom.tip_obecta else None,
                'sostoyanie_doma': i.dom.sostoyanie_doma.name if i.dom.sostoyanie_doma else None,
                'vladelez_doma': i.dom.vladelez_zdania.name if i.dom.vladelez_zdania else None,
            })
        return result
