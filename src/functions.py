import re
from typing import Optional


PATTERN = re.compile(r'''
    ^                            # beginning of string
    ((?:\w|-|\.)+@)              # at least 1 of (word character or '-' or '.'), followed by '@'
    ((?:\w|-|\.)+\.)+            # at least 1 of (at least 1 word character or '-' or '.', followed by '.'),
    (([a-z]){1,4}$)              # between 1 and 4 letters and end of string
    ''', re.VERBOSE)


def clean(string: str) -> str:
    return string.strip().lower()


def is_valid(string: str) -> bool:
    if re.search(PATTERN, string) is None:
        return False
    else:
        return True


def get_domain(string: str) -> Optional[str]:
    domain = None
    match = PATTERN.search(string)
    if match is not None:
        domain = match.group(2) + match.group(3)
    return domain
