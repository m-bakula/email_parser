import argparse
import os.path


# define help strings
ic_help: str = 'print the number of invalid emails, then one invalid email per line'
s_help: str = ('search for the string argument in emails, print the number of found emails, '
               'then one found email per line')
gbd_help: str = ('group emails by domain. then order groups and addresses within groups alphabetically and print them,'
                 'one per line')
feil_help: str = ('find emails not in the provided logs file, print the number of found emails, '
                  'then one found email per line')


class AppCli:
    """Represents a CLI app with its default configuration"""
    def __init__(self) -> None:
        self.arg_parser = argparse.ArgumentParser()
        # add args for -ic, -search, -gbd, -feil
        self.arg_parser.add_argument('-ic', '--incorrect-emails', dest='ic', action='store_true', help=ic_help)
        self.arg_parser.add_argument('-s', '--search', dest='search', type=str, action='store', help=s_help)
        self.arg_parser.add_argument('-gbd', '--group-by-domain', dest='gbd', action='store_true', help=gbd_help)
        self.arg_parser.add_argument('-feil', '--find-email-not-in-logs', dest='feil', type=str, action='store',
                                     help=feil_help)

        self.args = self.arg_parser.parse_args()
        self.args_tuple = (self.args.ic, self.args.search, self.args.gbd, self.args.feil)

    def validate_input(self) -> None:
        if self.args_tuple == (False, None, False, None):
            print('No option provided. Use --help to see all available options')
        elif self.args.search == '' or self.args.feil == '':
            print("Non-empty argument for option must be provided")
        elif self.args.feil is not None and not os.path.exists(self.args.feil):
            print(f'No log found file found at specified path: {self.args.feil}')
