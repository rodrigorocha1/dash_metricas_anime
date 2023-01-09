import requests
from typing import Dict


def requests_id_anime(self, ano, temporada: str) -> Dict[int, str]:
    url_id = self.__url + str(ano) + '/' + temporada + '?offset=0&limit=100'
    response = requests.get(url_id, headers=self.__header)

    return {
        "status_code": response.status_code,
        "json": response.json()
    }
