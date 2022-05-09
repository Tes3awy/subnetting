#!usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from getpass import getuser

from rich import print

from export_subnets import export_subnets
from read_subnets import read_subnets
from subnetting import subnetting


def main():
    try:
        # CSV file
        input_csv = input(f"\n- Subnets file [subnets.csv]: ") or "subnets.csv"
        gateway = int(
            input("- The gateway, first or last IP Address [0/1] [0]: ") or "0"
        )
        if gateway not in (0, 1):
            raise SystemExit(print("[red]0 and 1 are the only allowed values!"))
        # Excel file name
        workbook_name = (
            input("- Excel file to create [New-Schema.xlsx]: ") or "New-Schema.xlsx"
        )

        start = time.perf_counter()

        # Read CSV file
        subnets = read_subnets(file_path=input_csv)

        # Do Subnetting
        network_subnets = subnetting(input_subnets=subnets, gateway=gateway)

        # Export subnetting results to an Excel file
        export_subnets(subnets=network_subnets, workbook_name=workbook_name)

        d = round(time.perf_counter() - start, 2)
        print(f"Done in [blue]{d}[/blue] second(s)")

    except FileNotFoundError as e:
        raise SystemExit(print(f"[red]`{input_csv}` file does not exist!")) from e
    except KeyboardInterrupt:
        raise SystemExit(print(f"[yellow]Process interrupted by {getuser()}")) from None


if __name__ == "__main__":
    main()
