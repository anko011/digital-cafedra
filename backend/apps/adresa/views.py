from django.http import JsonResponse

from apps.adresa.models import Dom, Rayon


def my_view(request):
    from dadata import Dadata
    token = "dbdd762760a6d0a20ebdea53319b52df9617c10c"
    secret = "fcf37758cfda3e47b8d8b80ca2aac4f10ea1f8ac"
    dadata = Dadata(token, secret)

    # count = len(Dom.objects.filter(lat__isnull=True))
    count = len(Dom.objects.filter(flat_cadnum__isnull=True))
    i = 1
    # for dom in Dom.objects.filter(lat__isnull=True):
    for dom in Dom.objects.filter(flat_cadnum__isnull=True):

        try:
            result = dadata.clean("address", f'Москва {dom.uliza.name}, {dom.name}')
            # dom.lat = result['geo_lat']
            # dom.lon = result['geo_lon']
            dom.flat_cadnum = result['flat_cadnum']
            dom.json_dadata = result
            dom.save()
            print(f'{i}/{count} Москва {dom.uliza.name}, {dom.name} - ок')
        except Exception:
            print(f'{i}/{count}  Москва {dom.uliza.name}, {dom.name} - error')
        i += 1



    return JsonResponse({'status':'ок'})