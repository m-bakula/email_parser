from abc import ABC
from abc import abstractmethod
import csv

from src.functions import clean


class Reader(ABC):
    """Abstract base class for representing readers of various file types"""
    @abstractmethod
    def read_file(self) -> list[str]:
        """Should read the file's text and return its lines as a list of strings"""
        pass


class ReaderAbstract(Reader):
    """Generic reader class that defines common methods"""
    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath

    @abstractmethod
    def read_file(self) -> list[str]:
        pass


class ReaderTxt(ReaderAbstract):
    """Reader for a text file at given location"""
    def read_file(self) -> list[str]:
        with open(self.filepath, mode='r', encoding='utf-8') as txt_file:
            contents = []
            for line in txt_file:
                contents.append(clean(line))
        return contents


class ReaderCsv(ReaderAbstract):
    """Reader for a .csv file at given location"""
    def read_file(self) -> list[str]:
        with open(self.filepath, mode='r') as csv_file:
            contents = []
            dialect = csv.Sniffer().sniff(csv_file.readline(), delimiters=',|\t;')
            csv_file.seek(0)
            csv_reader = csv.DictReader(csv_file, dialect=dialect)
            for row in csv_reader:
                contents.append(clean(row['email']))
        return contents
