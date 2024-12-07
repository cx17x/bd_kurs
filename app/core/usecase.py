from abc import ABC, abstractmethod


class IUseCase(ABC):
    @abstractmethod
    def execute(self, dto):
        pass