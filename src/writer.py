from abc import ABC
from abc import abstractmethod


class Writer(ABC):
    """Abstract base class for representing writers to various outputs"""
    @staticmethod
    @abstractmethod
    def write_line(line: str) -> None:
        """Should write a single string to a given output"""
        pass

    @abstractmethod
    def write_contents(self, contents: list[str]) -> None:
        """Should write a list of strings, using write_line()"""
        pass


class WriterAbstract(Writer):
    """Generic writer class that defines common methods"""
    def __init__(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def write_line(line: str) -> None:
        pass

    def write_contents(self, contents: list[str]) -> None:
        for line in contents:
            self.write_line(line)


class WriterStdOut(WriterAbstract):
    """A writer to the standard output"""
    @staticmethod
    def write_line(line: str) -> None:
        print(line)
