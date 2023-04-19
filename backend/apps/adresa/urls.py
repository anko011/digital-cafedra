from django.urls import path

from apps.adresa.api import DomLV, DomDV, UlizaLV, UlizaDV, FotoDomaLV, FotoDomaDV, FailDomaLV, FailDomaDV, VideoDomaLV, \
    VideoDomaDV, NaseleniPunktLV, NaseleniPunktDV, RayonLV, RayonDV, TipObectaLV, TipObectaDV, SostoyanieDomaLV, \
    SostoyanieDomaDV, DopPoleDomaLV, DopPoleDomaDV, DopPoleNaDomeLV, DopPoleNaDomeDV

urlpatterns = [
    path('dom/', DomLV.as_view()),
    path('dom/<id>/', DomDV.as_view()),
    path('uliza/', UlizaLV.as_view()),
    path('uliza/<id>/', UlizaDV.as_view()),
    path('foto_doma/', FotoDomaLV.as_view()),
    path('foto_doma/<id>/', FotoDomaDV.as_view()),
    path('fail_doma/', FailDomaLV.as_view()),
    path('fail_doma/<id>/', FailDomaDV.as_view()),
    path('video_doma/', VideoDomaLV.as_view()),
    path('video_doma/<id>/', VideoDomaDV.as_view()),
    path('naseli_punkt/', NaseleniPunktLV.as_view()),
    path('naseli_punkt/<id>/', NaseleniPunktDV.as_view()),
    path('rayon/', RayonLV.as_view()),
    path('rayon/<id>/', RayonDV.as_view()),
    path('tip_obecta/', TipObectaLV.as_view()),
    path('tip_obecta/<id>/', TipObectaDV.as_view()),
    path('sostoyanie_doma/', SostoyanieDomaLV.as_view()),
    path('sostoyanie_doma/<id>/', SostoyanieDomaDV.as_view()),
    path('dop_pole_doma/', DopPoleDomaLV.as_view()),
    path('dop_pole_doma/<id>/', DopPoleDomaDV.as_view()),
    path('dop_pole_na_dome/', DopPoleNaDomeLV.as_view()),
    path('dop_pole_na_dome/<id>/', DopPoleNaDomeDV.as_view()),
]