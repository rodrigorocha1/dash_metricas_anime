from abc import abstractmethod, ABC


class WinterRequestsInterface(ABC):
    @abstractmethod
    def requests_id_anime(self) -> int:
        pass
