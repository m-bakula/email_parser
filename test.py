from src.parser import Parser
from src.commandworker import CommandWorker


parser_obj = Parser('emails')
parser_obj.parse_directory()

worker_obj = CommandWorker()

log_parser = Parser()
log_parser.parse_file('email-sent.logs', validate=False)


result = []

for address in parser_obj.get_contents():
    found: bool = worker_obj.is_in(address, log_parser.get_contents())
    if not found:
        result.append(address)

print(len(result), result)
