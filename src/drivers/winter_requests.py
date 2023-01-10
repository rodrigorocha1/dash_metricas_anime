import requests
from src.drivers.interfaces.winter_requests_interface import WinterRequestsInterface
import os
from dotenv import load_dotenv
from typing import Dict

load_dotenv()


class WinterRequest(WinterRequestsInterface):

    def __init__(self) -> None:
        self.__url = 'https://api.myanimelist.net/v2/anime/season/'
        self.__header = {'Authorization': os.environ['Authorization']}

    def requests_id_anime(self, ano, temporada: str, offset: int, limit: int) -> Dict[int, str]:
        url_id = self.__url + str(ano) + '/' + temporada + '?offset=' + str(offset) + '&limit=' + str(limit)
        response = requests.get(url_id, headers=self.__header,)
        return {
            'status_code': response.status_code,
            'json': response.json(),
            'paginacao' : response.json()['paging']
        }


if __name__ == '__main__':
    w = WinterRequest()
    print(w.requests_id_anime(2006, 'winter', 1, 100))
