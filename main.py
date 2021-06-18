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
                cprint("Sorry, but the input file MUST be a .csv file", "red")
            )
        # Excel file name
        workbook_name = (
            input("- Excel file w/o extension? [Defaults to IP-Schema]: ")
            or "IP-Schema"
        )
        if ".xlsx" in workbook_name:
            raise SystemExit(cprint("Please remove the .xlsx extension", "red"))
        # Excel sheet name
        worksheet_name = (
            input("- Worksheet name? [Defaults to IP Schema Worksheet]: ")
            or "IP Schema Worksheet"
        )

        # Read CSV file
        subnets = read_subnets(input_subnets)
        # Do Subnetting
        network_subnets = subnetting(subnets)
        # Export subnetting results to an Excel file
        export_subnets(network_subnets, workbook_name, worksheet_name)
    except FileNotFoundError as e:
        raise SystemExit(cprint(e, "red"))
    except KeyboardInterrupt:
        raise SystemExit(cprint("\nProcess interrupted by the user!", "yellow"))

    print("Done")


if __name__ == "__main__":
    main()
