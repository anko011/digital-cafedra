import datetime
import os

from dicttoxml import dicttoxml
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import Dom, DopPoleDoma, DopPoleNaDome, NaseleniPunkt, Okrug, Rayon, SostoyanieDoma, TipObecta, \
    Uliza
from apps.proekti.models import Proekt, DomPoProektu, DopPoleNaProekte, DopPoleProekta, ResheniePoProektu, \
    SoglosovaniePoProektu, SoglosovaniePoProektuDetail, StatusIspolnenia, StatusSoglasovania, TipResheniaPoProektu, \
    UchastnikRabochaiaGruppa
from apps.vladelzi_zdani.models import TipVladelza, VladelezZdania, Zastroyshik
from core.settings import MEDIA_ROOT


class RenderXmlApi(APIView):
    def get(self, request, model_dlya_xml):

        if model_dlya_xml == 'proekt':
            data = list(Proekt.objects.all().values())

        elif model_dlya_xml == 'dop_pole_doma':
            data = list(DopPoleDoma.objects.all().values())

        elif model_dlya_xml == 'dop_pole_na_doma':
            data = list(DopPoleNaDome.objects.all().values())

        elif model_dlya_xml == 'okrug':
            data = list(Okrug.objects.all().values())

        elif model_dlya_xml == 'rayon':
            data = list(Rayon.objects.all().values())

        elif model_dlya_xml == 'sostoyanie_doma':
            data = list(SostoyanieDoma.objects.all().values())

        elif model_dlya_xml == 'dop_pole_doma':
            data = list(DopPoleDoma.objects.all().values())

        elif model_dlya_xml == 'tip_obecta':
            data = list(TipObecta.objects.all().values())

        elif model_dlya_xml == 'uliza':
            data = list(Uliza.objects.all().values())

        elif model_dlya_xml == 'dom_po_proektu':
            data = list(DomPoProektu.objects.all().values())

        elif model_dlya_xml == 'dop_pole_na_proekte':
            data = list(DopPoleNaProekte.objects.all().values())

        elif model_dlya_xml == 'dop_pole_proekta':
            data = list(DopPoleProekta.objects.all().values())

        elif model_dlya_xml == 'dom':
            data = list(Dom.objects.all().values())

        elif model_dlya_xml == 'reshenie_po_proektu':
            data = list(ResheniePoProektu.objects.all().values())

        elif model_dlya_xml == 'soglosovanie_po_proektu':
            data = list(SoglosovaniePoProektu.objects.all().values())

        elif model_dlya_xml == 'soglosovanie_po_proektu_detail':
            data = list(SoglosovaniePoProektuDetail.objects.all().values())

        elif model_dlya_xml == 'status_ispolnenia':
            data = list(StatusIspolnenia.objects.all().values())

        elif model_dlya_xml == 'status_soglasovania':
            data = list(StatusSoglasovania.objects.all().values())

        elif model_dlya_xml == 'tip_reshenia_po_proektu':
            data = list(TipResheniaPoProektu.objects.all().values())

        elif model_dlya_xml == 'uchastnik_rabochaia_gruppa':
            data = list(UchastnikRabochaiaGruppa.objects.all().values())

        elif model_dlya_xml == 'tip_vladelza':
            data = list(TipVladelza.objects.all().values())

        elif model_dlya_xml == 'vladelez_zdania':
            data = list(VladelezZdania.objects.all().values())

        elif model_dlya_xml == 'zastroyshik':
            data = list(Zastroyshik.objects.all().values())

        else:
            return Response(status=400, data={'statusText':'Неизвестнвая таблица в БД'})


        os_dir_path = os.path.join(MEDIA_ROOT, 'xml')
        if not os.path.exists(os_dir_path):
            os.makedirs(os_dir_path)


        file_name = f"{model_dlya_xml} {datetime.datetime.now()}.xml"

        with open(os.path.join(os_dir_path, file_name), 'w') as xmlfile:
            xml = dicttoxml(data)
            xmlfile.write(xml.decode())


        return HttpResponseRedirect(f'/media/xml/{file_name}')