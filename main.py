from src.drivers.winter_requests import WinterRequest
from src.drivers.anime_stats import AnimeStats

wr = WinterRequest()
ans = AnimeStats()

lista_temporadas = ['winter', 'spring', 'summer', 'fall']
paginacao = 0
lista_animes = []
i = 1
for ano in range(2023, 2024):
    paginacao = 0
    for temporada in lista_temporadas:

        while True:

            b = wr.requests_id_anime(ano, temporada, paginacao)
            print('-----------')
            print(ano, temporada, paginacao)
            print('-----------')
            try:
                for anime in b['json']['data']:
                    d_animes = {
                        'id': anime['node']['id'],
                        'title': anime['node']['title']
                    }
                    lista_animes.append(d_animes)

                paginacao += 100
                if 'next' not in b['paginacao'].keys():
                    break
            except KeyError:
                break
            i += 1
        paginacao = 0

print(lista_animes)
