from abc import ABC, abstractmethod


class IDatabaseRepository(ABC):

    @abstractmethod
    def insert_data(self, dados):
        pass