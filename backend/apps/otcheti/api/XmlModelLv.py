import os

from django.http import HttpResponseRedirect
from docxtpl import DocxTemplate
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.adresa.models import Dom, DopPoleDoma, DopPoleNaDome, Okrug, Rayon, SostoyanieDoma, TipObecta, Uliza
from apps.proekti.models import Proekt, DomPoProektu, DopPoleProekta, ResheniePoProektu, SoglosovaniePoProektu, \
    SoglosovaniePoProektuDetail, StatusSoglasovania, TipResheniaPoProektu, UchastnikRabochaiaGruppa
from apps.vladelzi_zdani.models import TipVladelza, VladelezZdania, Zastroyshik
from core.settings import BASE_DIR, MEDIA_ROOT


class XmlModelLv(APIView):
    def get(self, request):
        base_url = "http://127.0.0.1:8000/api/otcheti/render_xml_api/"
        data = [
            {'label': Proekt._meta.verbose_name, 'url': base_url+ 'proekt/'},
            {'label': DopPoleDoma._meta.verbose_name, 'url': base_url +'dop_pole_doma/'},
            {'label': DopPoleNaDome._meta.verbose_name, 'url': base_url +'dop_pole_na_doma/'},
            {'label': Okrug._meta.verbose_name, 'url': base_url+'okrug/'},
            {'label': Rayon._meta.verbose_name, 'url': base_url+'rayon/'},
            {'label': SostoyanieDoma._meta.verbose_name, 'url': base_url+'sostoyanie_doma/'},
            {'label': DopPoleDoma._meta.verbose_name, 'url': base_url+'dop_pole_doma/'},
            {'label': TipObecta._meta.verbose_name, 'url': base_url+'tip_obecta/'},
            {'label': Uliza._meta.verbose_name, 'url': base_url+'uliza/'},
            {'label': DomPoProektu._meta.verbose_name, 'url': base_url+'dom_po_proektu/'},
            {'label': DopPoleProekta._meta.verbose_name, 'url': base_url+'dop_pole_proekta/'},
            {'label': Dom._meta.verbose_name, 'url': base_url+'dom/'},
            {'label': DomPoProektu._meta.verbose_name, 'url': base_url+'dom_po_proektu/'},
            {'label': ResheniePoProektu._meta.verbose_name, 'url': base_url+'reshenie_po_proektu/'},
            {'label': SoglosovaniePoProektu._meta.verbose_name, 'url': base_url+'soglosovanie_po_proektu/'},
            {'label': SoglosovaniePoProektuDetail._meta.verbose_name, 'url': base_url+'soglosovanie_po_proektu_detail/'},
            {'label': StatusSoglasovania._meta.verbose_name, 'url': base_url+'status_soglasovania/'},
            {'label': TipResheniaPoProektu._meta.verbose_name, 'url': base_url+'tip_reshenia_po_proektu/'},
            {'label': UchastnikRabochaiaGruppa._meta.verbose_name, 'url': base_url+'uchastnik_rabochaia_gruppa/'},
            {'label': TipVladelza._meta.verbose_name, 'url': base_url+'tip_vladelza/'},
            {'label': VladelezZdania._meta.verbose_name, 'url': base_url+'vladelez_zdania/'},
            {'label': Zastroyshik._meta.verbose_name, 'url': base_url+'zastroyshik/'},
        ]

        return Response(data)
