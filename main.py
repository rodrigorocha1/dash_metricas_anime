from tqdm import tqdm
import pickle
from src.drivers.winter_requests import WinterRequest
from src.infra.database_repository import DatabaseRepository

dr = DatabaseRepository()
wr = WinterRequest()

lista_temporadas = ['winter', 'spring', 'summer', 'fall']
paginacao = 0
lista_animes = []
i = 1
for ano in range(2006, 2024):
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

with open('lista_animes.pkl', 'wb') as arq_lista_animes:
    pickle.dump(lista_animes, arq_lista_animes)

with open('lista_animes.pkl', 'rb') as arg_pkl_lista_animes:
    pkl_lista_animes = pickle.load(arg_pkl_lista_animes)

lista_animes_stats = []
print(len(pkl_lista_animes))
for animes in tqdm(pkl_lista_animes):
    stats_anime = wr.requests_stats(animes['id'])
    lista_animes_stats.append(stats_anime)

with open('lista_animes_stats.pkl', 'wb') as arq_lista_animes_stasts:
    pickle.dump(lista_animes_stats, arq_lista_animes_stasts)


with open('lista_animes_stats.pkl', 'rb') as arg_pkl_lista_animes_stats:
    pkl_lista_animes_stats = pickle.load(arg_pkl_lista_animes_stats)

print(pkl_lista_animes_stats[0])

lista_status_anime_corrigida = []
for lista in pkl_lista_animes_stats:
    lista_status_anime_corrigida.append({chave: valor.encode("ascii", 'ignore').decode("ascii") if
    type(valor) == str else valor for chave, valor in lista.items()})

dr.insert_data_relacao_anime_main_picture(lista_status_anime_corrigida)
dr.insert_data_relacao_anime_statistics(lista_status_anime_corrigida)
dr.insert_data_relacao_genero_id_anime(lista_status_anime_corrigida)
dr.insert_data_relacao_studios_anime(lista_status_anime_corrigida)
dr.insert_data_dados_gerais(lista_status_anime_corrigida)
