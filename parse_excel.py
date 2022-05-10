#!usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from rich import print

from svi_generator import svi_generator

parser = ArgumentParser(
    prog="parse Excel",
    usage="python parse_excel.py --file path/to/excel/file",
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
    help="Path to an Excel file",
)

args = parser.parse_args()

try:
    f = svi_generator(excel_file=args.file)
except (FileNotFoundError, PermissionError) as e:
    raise SystemExit(print(f"[red]{e}")) from e
else:
    print(f"\n[green]Created {f.name} in cwd", end="\n\n")
