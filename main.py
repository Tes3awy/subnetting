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
            input(
                f"\n- Name of subnets file w/ file extension? [Defaults to subnets.csv]: "
            )
            or "subnets.csv"
        )
        if ".csv" not in input_subnets:
            raise SystemExit(cprint("Sorry, but input file MUST be a .csv file", "red"))
        # Excel file name
        workbook_name = (
            input(
                "- Name of Excel file w/o file extension? [Defaults to IP-Schema.xlsx]: "
            )
            or "IP-Schema"
        )
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
