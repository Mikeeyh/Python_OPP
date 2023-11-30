from abc import ABC, abstractmethod


class FileRule(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def execute(self):
        pass