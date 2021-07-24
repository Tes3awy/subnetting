#!usr/bin/env python3

from argparse import ArgumentParser

from colorama import init
from termcolor import colored, cprint

from svi_generator import svi_generator

init(autoreset=True)


parser = ArgumentParser(
    prog="parse excel",
    usage="python parse_excel.py --file <path to an Excel file>",
    description="An Excel file that contains subnets",
    epilog="Enjoy the program! :)",
    allow_abbrev=True,
    add_help=True,
)

parser.add_argument(
    "-f",
    "--file",
    metavar="Excel file",
    action="store",
    type=str,
    required=True,
    help="the path to an Excel file",
)

args = parser.parse_args()

try:
    svi_generator(excel_file=args.file)
except (FileNotFoundError, PermissionError) as e:
    raise SystemExit(colored(text=e, color="red"))
