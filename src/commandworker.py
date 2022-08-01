from collections import defaultdict

from src import functions


class CommandWorker:
    """A worker for processing lists of strings"""
    def __init__(self):
        pass

    @staticmethod
    def search(contents: list[str], query: str) -> list[str]:
        """Searches a list of strings (contents) for a query. Returns a list of strings that are a match"""
        results: list[str] = []
        for line in contents:
            if functions.search(query, line):
                results.append(line)
        return results

    @staticmethod
    def is_in(address: str, log_contents: list[str]) -> bool:
        """Checks if an address can be found in log_contents. Returns True or False accordingly"""
        found = False
        for line in log_contents:
            if functions.search(address, line):
                found = True
                break
        return found

    @staticmethod
    def group_by_domain(contents: list[str]) -> list[tuple[str, list[str]]]:
        """Takes a list of email addresses and groups them by domain. Returns a list of tuples: (domain, addr_list)"""
        domain_dict: defaultdict[str, list[str]] = defaultdict(list)
        for address in sorted(contents):
            domain_dict[functions.get_domain(address)].append(address)
        output: list[tuple[str, list[str]]] = []

        for domain in sorted(domain_dict.keys()):
            output.append((domain, sorted(domain_dict.get(domain))))
        return output
