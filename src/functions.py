import os.path
import re
from typing import Optional


PATTERN = re.compile(r'''
    ^                            # beginning of string
    ((?:\w|-|\.)+@)              # at least 1 of (word character or '-' or '.'), followed by '@'
    ((?:\w|-|\.)+\.)+            # at least 1 of (at least 1 word character or '-' or '.', followed by '.'),
    (([a-z]){1,4}$)              # between 1 and 4 letters and end of string
    ''', re.VERBOSE)


def get_extension(filepath: str) -> str:
    return os.path.splitext(filepath)[1]


def clean(string: str) -> str:
    return string.strip().lower()


def is_valid(string: str) -> bool:
    if re.search(PATTERN, string) is None:
        return False
    else:
        return True


def get_domain(string: str) -> Optional[str]:
    output = None
    if is_valid(string):
        match = PATTERN.search(string)
        output = match.group(2) + match.group(3)
    return output


def search(query: str, target: str) -> bool:
    if re.search(query, target, re.IGNORECASE) is None:
        return False
    else:
        return True
