from django.urls import path

from .api import DomPoProektuLV, DomPoProektuDV, ResheniePoProektuLV, ResheniePoProektuDV, StatusIspolneniaLV, \
    StatusIspolneniaDV, TipResheniaPoProektuLV, TipResheniaPoProektuDV, ProektLV, ProektDV, UchastnikRabochaiaGruppaLV, \
    UchastnikRabochaiaGruppaDV, DopPoleNaProekteLV, DopPoleNaProekteDV, DopPoleProektaLV, DopPoleProektaDV, KalendarLv

urlpatterns = [
    path('dom_po_proektu/', DomPoProektuLV.as_view()),
    path('dom_po_proektu/<id>/', DomPoProektuDV.as_view()),
    path('reshenie_po_proektu/', ResheniePoProektuLV.as_view()),
    path('reshenie_po_proektu/<id>/', ResheniePoProektuDV.as_view()),
    path('status_ispolnenia/', StatusIspolneniaLV.as_view()),
    path('status_ispolnenia/<id>/', StatusIspolneniaDV.as_view()),
    path('tip_reshenia_po_proektu/', TipResheniaPoProektuLV.as_view()),
    path('tip_reshenia_po_proektu/<id>/', TipResheniaPoProektuDV.as_view()),
    path('proekt/', ProektLV.as_view()),
    path('proekt/<id>/', ProektDV.as_view()),
    path('uchastnik_rabochaia_gruppa/', UchastnikRabochaiaGruppaLV.as_view()),
    path('uchastnik_rabochaia_gruppa/<id>/', UchastnikRabochaiaGruppaDV.as_view()),
    path('dop_pole_na_proekte/', DopPoleNaProekteLV.as_view()),
    path('dop_pole_na_proekte/<id>/', DopPoleNaProekteDV.as_view()),
    path('dop_pole_proekta/', DopPoleProektaLV.as_view()),
    path('dop_pole_proekta/<id>/', DopPoleProektaDV.as_view()),
    path('kalendar/', KalendarLv.as_view()),
]