from src.drivers.interfaces.anime_stats_interface_interface import AnimeStatsinterface
import os
from dotenv import load_dotenv
import requests
from typing import Dict
load_dotenv()


class AnimeStats(AnimeStatsinterface):
    def __init__(self) -> None:
        self.__url = 'https://api.myanimelist.net/v2/anime/'
        self.__header = {'Authorization': os.environ['Authorization']}

    def obter_stats(self, id_anime: int) -> Dict:
        url = self.__url + str(
            id_anime) + '?fields=id,title,main_picture,start_date,end_date,synopsis,mean,rank,num_list_users,' \
                        'num_scoring_users,media_type,status,genres,num_episodes,start_season,source,rating,' \
                        'average_episode_duration,pictures,studios,statistics,num_list_users '
        response = requests.get(url=url, headers=self.__header, )
        return response.json()


if __name__ == '__main__':
    anime_stats = AnimeStats()
    a = anime_stats.obter_stats(10087)
    print(a)
