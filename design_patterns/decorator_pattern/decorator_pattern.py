from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def writeData(self, data):
        pass

    @abstractmethod
    def readData(self) -> str:
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self._file = filename

    def writeData(self, data):
        with open(self._file, "w") as file:
            file.write(data)
        pass

    def readData(self) -> str:
        with open(self._file, "r") as file:
            return file.readline()


class EncryptionDecorator(DataSource):
    def __init__(self, writer):
        self.writer = writer

    def writeData(self, data):
        data = f"Encrypted {data}"
        self.writer.writeData(data)

    def readData(self) -> str:
        line = self.writer.readData()
        line = line.replace("Encrypted", "")
        return line


encryption = EncryptionDecorator(FileDataSource("example.txt"))
encryption.writeData("Hello")
print(encryption.readData())

