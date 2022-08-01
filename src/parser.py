import os
from typing import Type

from src.functions import is_valid
from src.reader import ReaderAbstract
from src.reader import ReaderCsv
from src.reader import ReaderTxt


class Parser:
    """A class for parsing files and directories with text contents for email addresses"""
    # dictionary mapping all supported file extensions to an appropriate Reader class
    ext_to_reader: dict[str, ReaderAbstract] = {'.txt': ReaderTxt, '.log': ReaderTxt, '.logs': ReaderTxt,
                                                '.csv': ReaderCsv}

    def __init__(self, directory: str = os.getcwd()):
        self.directory: str = os.path.abspath(directory)
        self.files: list[str] = []
        if os.path.isdir(self.directory):
            self.files = [os.path.join(directory, filename) for filename in os.listdir(self.directory)]

        self.contents: set[str] = set()                     # is a set of strings, so no duplicates occur
        self.invalid_contents: list[str] = []

    def get_contents(self) -> list[str]:
        return list(self.contents)

    def get_invalid(self) -> list[str]:
        return self.invalid_contents

    def parse_file(self, file: str, validate: bool = True) -> None:
        filepath = os.path.abspath(file)
        extension = os.path.splitext(filepath)[1]

        if extension in self.ext_to_reader.keys():
            reader_class: Type[ReaderAbstract] = self.ext_to_reader.get(extension)
            current_file: ReaderAbstract = reader_class(filepath)
            new_contents: list[str] = current_file.read_file()

            if validate:
                for address in new_contents:
                    if is_valid(address):
                        self.contents.add(address)
                    else:
                        self.invalid_contents.append(address)
            else:
                self.contents.update(new_contents)

    def parse_directory(self) -> None:
        for file in self.files:
            self.parse_file(file)
