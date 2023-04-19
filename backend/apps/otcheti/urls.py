from django.urls import path

from apps.otcheti.api import RenderProtocolSoglasovaniaApi, RenderXmlApi, XmlModelLv, RenderPovestkiApi

urlpatterns = [
    path('render_protocol_soglasovania/<soglosovanie_po_proektu_id>/', RenderProtocolSoglasovaniaApi.as_view()),
    path('render_povestka/', RenderPovestkiApi.as_view()),
    path('render_xml_api/<model_dlya_xml>/', RenderXmlApi.as_view()),
    path('xml_model_lv/', XmlModelLv.as_view()),
]
