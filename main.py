from src.appcli import AppCli
from src.commandworker import CommandWorker
from src.parser import Parser
from src.writer import WriterStdOut

# instantiate cli app, parser, writer and validate inputs
app = AppCli()
app.validate_input()

parser_obj = Parser('emails')
parser_obj.parse_directory()

worker_obj = CommandWorker()
writer_obj = WriterStdOut()


# define command functions
def incorrect_emails() -> None:
    result: list[str] = ['\t' + line for line in parser_obj.get_invalid()]
    writer_obj.write_line(f'{len(result)} INVALID EMAILS:')
    writer_obj.write_contents(result)


def search_for() -> None:
    result: list[str] = ['\t' + line for line in worker_obj.search(parser_obj.get_contents(), app.args.search)]
    writer_obj.write_line(f"{len(result)} EMAILS FOUND WITH '{app.args.search}' PHRASE:")
    writer_obj.write_contents(result)


def group_by_domain() -> None:
    result: list[str] = []
    for domain, addresses in worker_obj.group_by_domain(parser_obj.get_contents()):
        result.append(f'Domain {domain} ({len(addresses)}):')
        result.extend(['\t' + line for line in addresses])
    writer_obj.write_contents(result)


def find_not_in_logs() -> None:
    result: list[str] = []
    log_parser = Parser()
    log_parser.parse_file(app.args.feil, validate=False)
    for address in parser_obj.get_contents():
        found: bool = worker_obj.is_in(address, log_parser.get_contents())
        if not found:
            result.append(address)

    writer_obj.write_line(f'{len(result)} EMAILS NOT SENT:')
    writer_obj.write_contents(['\t' + line for line in sorted(result)])


# run command functions
arg_to_comm: dict = {app.args.ic: incorrect_emails, app.args.search: search_for, app.args.gbd: group_by_domain,
                     app.args.feil: find_not_in_logs}
for arg, cmd in arg_to_comm.items():
    if arg:
        cmd()
