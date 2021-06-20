#!usr/bin/env python3

from colorama import init
from termcolor import cprint

from export_subnets import export_subnets
from read_subnets import read_subnets
from subnetting import subnetting

init(autoreset=True)


def main():
    try:
        # CSV file
        input_subnets = (
            input(f"\n- CSV file w/ extension? [Defaults to subnets.csv]: ")
            or "subnets.csv"
        )
        if ".csv" not in input_subnets:
            raise SystemExit(
                cprint("Sorry! The input file MUST include .csv extension", "red")
            )
        gateway = int(
            input("- Gateway first or last IP Address? [0/1] [Defaults to 0]: ") or "0"
        )
        if gateway not in (0, 1):
            raise SystemExit(
                cprint(
                    "0 and 1 are the only allowed values! 0: First IP, 1: Last IP",
                    "red",
                )
            )
        # Excel file name
        workbook_name = (
            input("- Excel file w/o extension? [Defaults to IP-Schema]: ")
            or "IP-Schema"
        )
        if ".xlsx" in workbook_name:
            raise SystemExit(cprint("Oops! Please remove the .xlsx extension", "red"))
        # Excel sheet name
        worksheet_name = (
            input("- Worksheet name? [Defaults to IP Schema Worksheet]: ")
            or "IP Schema Worksheet"
        )

        # Microsoft Excel does not allow worksheet name longer than 31 chars
        if len(worksheet_name) > 31:
            worksheet_name = worksheet_name[0:31]

        # Read CSV file
        subnets = read_subnets(input_subnets)

        # Do Subnetting
        network_subnets = subnetting(subnets, gateway)

        # Export subnetting results to an Excel file
        export_subnets(network_subnets, workbook_name, worksheet_name)

    except FileNotFoundError:
        raise SystemExit(
            cprint(f"main.py: {input_subnets} file does not exist!", "red")
        )
    except KeyboardInterrupt:
        raise SystemExit(cprint("\nProcess interrupted by the user!", "yellow"))

    print("Done")


if __name__ == "__main__":
    main()
