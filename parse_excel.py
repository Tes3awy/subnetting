#!usr/bin/env python3

import os
from argparse import ArgumentParser
from datetime import date

from colorama import init
from termcolor import cprint

from svi_generator import svi_generator

init(autoreset=True)

today = date.today()

parser = ArgumentParser(
    description="An Excel file that contains subnets",
    epilog="Enjoy the program! :)",
    allow_abbrev=True,
    add_help=True,
)

parser.add_argument(
    "-f",
    "--file",
    metavar="file",
    action="store",
    type=str,
    required=True,
    help="Path to/Name of an Excel file",
)

args = parser.parse_args()

if ".xlsx" not in args.file:
    raise SystemExit(
        cprint("Invalid input file. The file MUST end with .xlsx extension", "red")
    )
if not os.path.isfile(args.file):
    raise SystemExit(cprint(f"{args.file} does not exist!", "red"))

svi_generator(args.file)

cprint(
    f'Created {args.file.replace(".xlsx", "")}_svi_template_{today}.txt successfully.',
    "green",
)
