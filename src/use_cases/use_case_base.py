from abc import ABC, abstractmethod


class UseCaseBase(ABC):
    @abstractmethod
    def execute(self):
        pass
