#!usr/bin/env python3

import time
from getpass import getuser

from colorama import init
from termcolor import colored, cprint

from export_subnets import export_subnets
from read_subnets import read_subnets
from subnetting import subnetting

init(autoreset=True)


def main():
    try:
        # CSV file
        input_csv = input(f"\n- CSV file [subnets.csv]: ") or "subnets.csv"
        gateway = int(
            input("- The gateway, first or last IP Address [0/1] [0]: ") or "0"
        )
        if gateway not in (0, 1):
            raise SystemExit(
                colored(text="0 and 1 are the only allowed values!", color="red")
            )
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

        end = time.perf_counter()

        delta = round(end - start, 2)
        cprint(text=f"Finished in {delta} second(s)", on_color="on_blue")

    except FileNotFoundError:
        raise SystemExit(
            colored(text=f"`{input_csv}` file does not exist!", color="red")
        )
    except KeyboardInterrupt:
        raise SystemExit(
            colored(text=f"Process interrupted by {getuser()}", color="yellow")
        )


if __name__ == "__main__":
    main()
