from abc import abstractmethod, ABC


class AnimeStatsinterface(ABC):
    @abstractmethod
    def obter_stats(self) -> int:
        pass
