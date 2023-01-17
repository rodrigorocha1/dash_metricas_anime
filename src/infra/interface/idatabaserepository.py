from abc import ABC, abstractmethod
from typing import List


class IDatabaseRepository(ABC):

    @abstractmethod
    def insert_data_relacao_anime_main_picture(self, dados: List):
        pass

    @abstractmethod
    def insert_data_relacao_genero_id_anime(self, dados: List):
        pass

    @abstractmethod
    def insert_data_relacao_url_figura_id_anime(self, dados: List):
        pass

    @abstractmethod
    def insert_data_relacao_studios_anime(self, dados: List):
        pass

    @abstractmethod
    def insert_data_relacao_anime_statistics(self, dados: List):
        pass

    @abstractmethod
    def insert_data_dados_gerais(self, dados: List):
        pass


