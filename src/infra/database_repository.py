from src.infra.interface.idatabaserepository import IDatabaseRepository
import csv
from typing import List


class DatabaseRepository(IDatabaseRepository):
    @classmethod
    def insert_data(cls, lista_stats_animes: List):
        nome_colunas_genero = ['id_anime', 'id_genero', 'nome_genero']
        nome_colunas_id_figura = ['id_anime', 'medium', 'large']
        nome_colunas_studio = ['id_anime', 'id_studio', 'name']
        nomes_colunas_img = ['id_anime', 'medium_img', 'large_img', 'season', 'year']

        with open('../../src/arquivos_csv/relacao_anime_main_picture.csv', 'a', newline='') as relacao_anime_main_picture:

            cursor = csv.writer(relacao_anime_main_picture, delimiter=';')
            cursor.writerow(nomes_colunas_img)
            for anime_url_img in lista_stats_animes:
                cursor.writerow([anime_url_img['id'], anime_url_img['main_picture']['medium'],
                                 anime_url_img['main_picture']['large'], anime_url_img['start_season']['year'],
                                 anime_url_img['start_season']['season']])
            relacao_anime_main_picture.close()

        with open('../../src/arquivos_csv/relacao_genero_id_anime.csv', 'a', newline='') as relacao_genero_id_anime:

            cursor = csv.writer(
                relacao_genero_id_anime,
                delimiter=';'
            )
            cursor.writerow(nome_colunas_genero)
            for stats_anime in lista_stats_animes:
                for genero in stats_anime['genres']:
                    cursor.writerow([stats_anime['id'], genero['id'], genero['name']])
            relacao_genero_id_anime.close()

        with open('../../src/arquivos_csv/relacao_url_figura_id_anime.csv', 'a',
                  newline='') as relacao_url_figura_id_anime:
            cursor = csv.writer(
                relacao_url_figura_id_anime,
                delimiter=';'
            )
            cursor.writerow(nome_colunas_id_figura)
            for stats_anime in lista_stats_animes:
                for picture in stats_anime['pictures']:
                    cursor.writerow([stats_anime['id'], picture['medium'], picture['large']])
            relacao_url_figura_id_anime.close()

        with open('../../src/arquivos_csv/relacao_studios_anime.csv', 'a', newline='') as relacao_studios_anime:

            cursor = csv.writer(
                relacao_studios_anime,
                delimiter=';'
            )
            cursor.writerow(nome_colunas_studio)
            for stats_anime in lista_stats_animes:
                for studio in stats_anime['studios']:
                    cursor.writerow([stats_anime['id'], studio['id'], studio['name']])
            relacao_studios_anime.close()

        with open('../../src/arquivos_csv/relacao_anime_statistics.csv', 'a', newline='') as relacao_anime_statistics:
            nomes_colunas_status = ['id_anime', 'watching', 'completed', 'on_hold', 'dropped', 'plan_to_watch']
            cursor = csv.writer(relacao_anime_statistics, delimiter=';')
            cursor.writerow(nomes_colunas_status)
            for stats_anime in lista_stats_animes:
                cursor.writerow([stats_anime['id'], stats_anime['statistics']['status']['watching'],
                                 stats_anime['statistics']['status']['completed'],
                                 stats_anime['statistics']['status']['on_hold'],
                                 stats_anime['statistics']['status']['dropped'],
                                 stats_anime['statistics']['status']['plan_to_watch']])
            relacao_anime_statistics.close()

        with open('../../src/arquivos_csv/dados_gerais.csv', 'a', newline='') as dados_gerais:
            lista_nomes_colunas = lista_stats_animes
            del lista_nomes_colunas[0]['studios']
            del lista_nomes_colunas[0]['genres']
            del lista_nomes_colunas[0]['pictures']
            del lista_nomes_colunas[0]['statistics']
            del lista_nomes_colunas[0]['main_picture']
            del lista_nomes_colunas[0]['start_season']
            nome_colunas = lista_nomes_colunas[0].keys()
            escritor = csv.DictWriter(
                dados_gerais,
                fieldnames=nome_colunas,
                delimiter=';'
            )
            escritor.writeheader()
            for chave, stat_anime in enumerate(lista_stats_animes):
                if chave == 1:
                    del stat_anime['studios']
                    del stat_anime['genres']
                    del stat_anime['pictures']
                    del stat_anime['main_picture']
                    del stat_anime['statistics']
                    del stat_anime['start_season']
                escritor.writerow(stat_anime)
            dados_gerais.close()
