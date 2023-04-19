from django.urls import path

from .api import ZastroyshikLV, ZastroyshikDV, TipVladelzaLV, TipVladelzaDV, VladelezZdaniaLV, VladelezZdaniaDV

urlpatterns = [
    path('zastroyshik/', ZastroyshikLV.as_view()),
    path('zastroyshik/<id>/', ZastroyshikDV.as_view()),
    path('tip_vladelza/', TipVladelzaLV.as_view()),
    path('tip_vladelza/<id>/', TipVladelzaDV.as_view()),
    path('vladelez_zdania/', VladelezZdaniaLV.as_view()),
    path('vladelez_zdania/<id>/', VladelezZdaniaDV.as_view()),
]