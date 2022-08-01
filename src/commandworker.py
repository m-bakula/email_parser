from collections import defaultdict

from src.functions import get_domain


class CommandWorker:
    """A worker for processing lists of strings"""
    def __init__(self):
        pass

    @staticmethod
    def search(contents: list[str], query: str) -> list[str]:
        """Searches a list of strings (contents) for a query. Returns a list of strings that are a match"""
        results: list[str] = list(filter(lambda line: (query in line), contents))
        return results

    @staticmethod
    def is_in(query: str, contents: list[str]) -> bool:
        """Checks if a query can be found in contents. Returns True or False accordingly"""
        found = False
        for line in contents:
            if query in line:
                found = True
                break
        return found

    @staticmethod
    def group_by_domain(contents: list[str]) -> list[tuple[str, list[str]]]:
        """Takes a list of email addresses and groups them by domain. Returns a list of tuples: (domain, addr_list)"""
        domain_dict: defaultdict[str, list[str]] = defaultdict(list)
        for address in sorted(contents):
            domain_dict[get_domain(address)].append(address)

        output: list[tuple[str, list[str]]] = []
        for domain in sorted(domain_dict.keys()):
            output.append((domain, sorted(domain_dict.get(domain))))
        return output
