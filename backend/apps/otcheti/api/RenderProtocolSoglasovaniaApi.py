import os

from django.http import HttpResponseRedirect
from docxtpl import DocxTemplate
from rest_framework.views import APIView

from apps.adresa.models import Dom
from core.settings import BASE_DIR, MEDIA_ROOT


class RenderProtocolSoglasovaniaApi(APIView):
    def get(self, request, soglosovanie_po_proektu_id):
        # try:
        #     soglosovanie_po_proektu = SoglosovaniePoProektu.objects.get(id=soglosovanie_po_proektu_id)
        # except Exception:
        #     return Response(status=400, data={'statusText':'Согласование не найдено'})

        path = os.path.join(BASE_DIR, 'apps', 'otcheti', 'templates', 'otcheti',  'protocol_soglasovania.docx')
        doc = DocxTemplate(path)

        # proekt = soglosovanie_po_proektu.proekt

        # komisia = proekt.uchastnikrabochaiagruppa_set.all()
        reshenia_soglasuushih = [
            {'fio_uchastnika_gruppi':'Иванов', 'dolznost_uchastnika_gruppi':'Инспектор ГЖИ', 'reshenie':'За'},
            {'fio_uchastnika_gruppi':'Петров', 'dolznost_uchastnika_gruppi':'Инспектор ГЖИ', 'reshenie':'За'},
            {'fio_uchastnika_gruppi':'Сидоров', 'dolznost_uchastnika_gruppi':'Представитель УК Лидер', 'reshenie':'Против'},
            {'fio_uchastnika_gruppi':'Стрельцова', 'dolznost_uchastnika_gruppi':'Представитель фонда капитального ремонта', 'reshenie':'За'},
            {'fio_uchastnika_gruppi':'Стрельцова', 'dolznost_uchastnika_gruppi':'Представитель фонда капитального ремонта', 'reshenie':'Воздержались'},
        ]

        soglasovania = [
            {'name':'За', 'kolvo':3},
            {'name':'Против', 'kolvo':1},
            {'name':'Воздержались', 'kolvo':1},
        ]

        data = {
            'data': '25.02.2022',
            'reshenia_soglasuushih': reshenia_soglasuushih,
            'resenie': 'Провести капитальный ремонт фундамента',
            'adres': Dom.objects.first().get_full_adres(),
            'soglasovania': soglasovania,
        }
        doc.render(data)

        os_dir_path = os.path.join(MEDIA_ROOT, 'otchet')
        if not os.path.exists(os_dir_path):
            os.makedirs(os_dir_path)

        file_name = f"soglasovanie_{soglosovanie_po_proektu_id}.docx"
        doc.save(os.path.join(os_dir_path, file_name))

        return HttpResponseRedirect(f'/media/otchet/{file_name}')