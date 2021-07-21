#!usr/bin/env python3

import os
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

if not args.file.endswith(".xlsx"):
    raise SystemExit(colored("\nInvalid input file. The file MUST be a .xlsx", "red"))
if not os.path.isfile(args.file):
    raise SystemExit(colored(f"{args.file} does not exist!", "red"))

svi_generator(args.file)  # Execute the svi_generator

cprint(
    f'\nCreated {args.file.replace(".xlsx", "")}-svi-template.txt successfully.',
    "green",
)
