import requests
from src.drivers.interfaces.winter_requests_interface import WinterRequestsInterface
import os
from dotenv import load_dotenv
from typing import Dict
from time import sleep
load_dotenv()


class WinterRequest(WinterRequestsInterface):

    def __init__(self) -> None:
        self.__url = 'https://api.myanimelist.net/v2/anime/'
        self.__header = {'Authorization': os.environ['Authorization']}

    def requests_id_anime(self, ano, temporada: str, offset: int) -> Dict[int, str]:
        url_id = self.__url + 'season/' + str(ano) + '/' + temporada + '?offset=' + str(offset) + '&limit=100'
        response = requests.get(url_id, headers=self.__header, )
        try:
            retorno = {
                'status_code': response.status_code,
                'json': response.json(),

                'paginacao': response.json()['paging']

            }
        except:
            retorno = {
                'status_code': response.status_code,
                'json': response.json(),

                'paginacao': 0

            }
        return retorno

    def requests_stats(self, id: str):
        url_chamada = self.__url + str(id) + '?fields=id,title,main_picture,start_date,synopsis,mean,rank,' \
                                             'num_list_users,num_scoring_users,media_type,status,genres,num_episodes,' \
                                             'start_season,source,rating,average_episode_duration,pictures,studios,' \
                                             'statistics,num_list_users '

        req_stats = requests.get(url_chamada, headers=self.__header)
        sleep(0.5)
        return req_stats.json()


if __name__ == '__main__':
    w = WinterRequest()
    j = w.requests_id_anime(2023, 'spring', 0)
    print(j['paginacao'], len(j['paginacao']))
    # stats_anime = w.requests_stats(42361)
    # print(stats_anime['id'])
    # for generos in stats_anime['genres']:
    #     print(generos['id'])
    #     print(generos['name'])
