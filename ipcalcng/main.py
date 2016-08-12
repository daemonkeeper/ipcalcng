import argparse

from ipcalcng.core import log, set_log_debug, set_log_info
from ipcalcng.calc import parse_prefix
import ipcalcng.output


def main():
    arguments = argparse.ArgumentParser(description="IPv4/IPv6 subnet calculator (new generation) ")

    color_arguments = arguments.add_mutually_exclusive_group()
    color_arguments.add_argument("-n", "--nocolor", action='store_true', default=False, help="Don't display ANSI "
                                                                                             "color codes")
    color_arguments.add_argument("-c", "--color", action='store_true', default=True, help='Display ANSI color codes '
                                                                                          '(default)')

    arguments.add_argument("-b", "--nobinary", action='store_true', help="Suppress the bitwise output")
    arguments.add_argument("-v", "--version", action='store_true', help="print version number and exit")
    arguments.add_argument("-d", "--verbose", action='count', default=0,
                           help="show debugging output. Repeat twice for even more output")

    arguments.add_argument("prefix", action='store', nargs='+')

    modes = arguments.add_mutually_exclusive_group()
    modes.add_argument("-s", "--split", action='store', nargs='+')
    modes.add_argument("-r", "--range", action='store_true',)

    args = arguments.parse_args()

    if args.verbose == 1:
        set_log_info()
    elif args.verbose >= 2:
        set_log_debug()
    log.debug("got args: %s" % args)

    prefixes = parse_prefix(args.prefix)

    for prefix in prefixes:
        p = ipcalcng.output.TextOutput(args, prefix)
        p.print_out()




