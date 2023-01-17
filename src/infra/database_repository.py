import os
from src.infra.interface.idatabaserepository import IDatabaseRepository
import csv
from typing import List, Dict, Any


class DatabaseRepository(IDatabaseRepository):

    @classmethod
    def insert_data_relacao_anime_main_picture(cls, dados: List):
        nomes_colunas_img = ['id_anime', 'medium_img', 'large_img', 'season', 'year']
        with open(os.getcwd() + '\\src\\arquivos_csv\\relacao_anime_main_picture.csv', 'a', newline='',
                  encoding='latin-1') \
                as relacao_anime_main_picture:
            cursor = csv.writer(relacao_anime_main_picture, delimiter=';')
            cursor.writerow(nomes_colunas_img)
            for anime_url_img in dados:
                print(anime_url_img)
                try:
                    cursor.writerow([anime_url_img['id'], anime_url_img['main_picture']['medium'],
                                     anime_url_img['main_picture']['large'], anime_url_img['start_season']['year'],
                                     anime_url_img['start_season']['season']])
                except Exception as e:
                    print(e)
                    continue
            relacao_anime_main_picture.close()

    @classmethod
    def insert_data_relacao_genero_id_anime(cls, dados_id: List):
        nome_colunas_genero = ['id_anime', 'id_genero', 'nome_genero']
        with open(os.getcwd() + '\\src\\arquivos_csv\\relacao_genero_id_anime.csv',
                  'a',
                  newline='',
                  encoding='UTF-8') \
                as relacao_genero_id_anime:

            cursor = csv.writer(
                relacao_genero_id_anime,
                delimiter=';'
            )
            cursor.writerow(nome_colunas_genero)
            for stats_anime in dados_id:

                try:
                    for genero in stats_anime['genres']:
                        try:
                            cursor.writerow([stats_anime['id'], genero['id'], genero['name']])
                        except UnicodeEncodeError:
                            continue
                except UnicodeEncodeError:
                    continue
                except:
                    continue

            relacao_genero_id_anime.close()

    @classmethod
    def insert_data_relacao_url_figura_id_anime(self, dados_url: List):
        nome_colunas_id_figura = ['id_anime', 'medium', 'large']
        with open(os.getcwd() + '\\src\\arquivos_csv\\relacao_url_figura_id_anime.csv', 'a',
                  newline='') as relacao_url_figura_id_anime:
            cursor = csv.writer(
                relacao_url_figura_id_anime,
                delimiter=';'
            )
            cursor.writerow(nome_colunas_id_figura)
            for stats_anime in dados_url:
                for picture in stats_anime['pictures']:
                    cursor.writerow([stats_anime['id'], picture['medium'], picture['large']])
            relacao_url_figura_id_anime.close()

    @classmethod
    def insert_data_relacao_studios_anime(cls, dados_studios: List):
        nome_colunas_studio = ['id_anime', 'id_studio', 'name']
        with open(os.getcwd() + '\\src\\arquivos_csv\\relacao_studios_anime.csv', 'a', newline='',
                  encoding='ISO-8859-1') \
                as relacao_studios_anime:

            cursor = csv.writer(
                relacao_studios_anime,
                delimiter=';'
            )
            cursor.writerow(nome_colunas_studio)
            for stats_anime in dados_studios:
                try:
                    for studio in stats_anime['studios']:
                        try:
                            cursor.writerow([stats_anime['id'], studio['id'], studio['name']])
                        except:
                            continue
                except:
                    continue
            relacao_studios_anime.close()

    @classmethod
    def insert_data_relacao_anime_statistics(cls, dados_stats: List):
        with open(os.getcwd() + '\\src\\arquivos_csv\\relacao_anime_statistics.csv', 'a', newline='',
                  encoding='ISO-8859-1') \
                as relacao_anime_statistics:
            nomes_colunas_status = ['id_anime', 'watching', 'completed', 'on_hold', 'dropped', 'plan_to_watch']
            cursor = csv.writer(relacao_anime_statistics, delimiter=';')
            cursor.writerow(nomes_colunas_status)
            for stats_anime in dados_stats:

                try:
                    cursor.writerow([stats_anime['id'], stats_anime['statistics']['status']['watching'],
                                     stats_anime['statistics']['status']['completed'],
                                     stats_anime['statistics']['status']['on_hold'],
                                     stats_anime['statistics']['status']['dropped'],
                                     stats_anime['statistics']['status']['plan_to_watch']])
                except KeyError:
                    continue

            relacao_anime_statistics.close()

    @classmethod
    def insert_data_dados_gerais(cls, dados_gerais_entrada: List):

        with open(os.getcwd() + '\\src\\arquivos_csv\\dados_gerais.csv', 'a', newline='',
                  encoding='ISO-8859-1') as dados_gerais:
            lista_nomes_colunas = dados_gerais_entrada
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
            for chave, stat_anime in enumerate(dados_gerais_entrada):
                if chave == 0:
                    escritor.writerow(stat_anime)
                else:
                    try:
                        del stat_anime['studios']
                        del stat_anime['genres']
                        del stat_anime['pictures']
                        del stat_anime['main_picture']
                        del stat_anime['statistics']
                        del stat_anime['start_season']
                        escritor.writerow(stat_anime)
                    except Exception as e:
                        with open(os.getcwd() + '\\src\\arquivos_csv\\erro.txt', 'a', newline='',
                                  encoding='latin-1') \
                                as doc_error:

                            cursor = csv.writer(doc_error, delimiter=';')
                            cursor.writerow([['ERRO'], [stat_anime], [e]])

                            doc_error.close()
                        continue

            dados_gerais.close()

