import abc


class Algorithm(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    def algorithm(self):
        pass
