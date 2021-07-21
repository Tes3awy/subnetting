#!usr/bin/env python3

from getpass import getuser

from colorama import init
from termcolor import colored

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
                colored("Sorry! The input file MUST include .csv extension", "red")
            )
        gateway = int(
            input("- The gateway, first or last IP Address? [0/1] [Defaults to 0]: ")
            or "0"
        )
        if gateway not in (0, 1):
            raise SystemExit(
                colored(
                    "0 and 1 are the only allowed values! 0: First IP, 1: Last IP",
                    "red",
                )
            )
        # Excel file name
        workbook_name = (
            input("- Excel file w/o extension? [Defaults to IP-Schema]: ")
            or "IP-Schema"
        )
        if workbook_name.endswith(".xlsx"):
            raise SystemExit(colored("Oops! Please remove the .xlsx extension", "red"))
        # Excel sheet name
        worksheet_name = (
            input("- Worksheet name? [Defaults to IP Schema Worksheet]: ")
            or "IP Schema Worksheet"
        )

        # Read CSV file
        subnets = read_subnets(file_path=input_subnets)

        # Do Subnetting
        network_subnets = subnetting(input_subnets=subnets, gateway=gateway)

        # Export subnetting results to an Excel file
        export_subnets(
            subnets=network_subnets,
            workbook_name=workbook_name,
            worksheet_name=worksheet_name[:31],
        )

    except FileNotFoundError:
        raise SystemExit(
            colored(f"main.py: {input_subnets} file does not exist!", "red")
        )
    except KeyboardInterrupt:
        raise SystemExit(colored(f"\nProcess interrupted by {getuser()}", "yellow"))

    print("Done")


if __name__ == "__main__":
    main()
