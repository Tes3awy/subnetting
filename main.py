#!usr/bin/env python3

from colorama import init
from termcolor import cprint

from export_subnets import export_subnets
from subnetting import subnetting

init(autoreset=True)


def main():
    input_subnets = ""
    try:
        # Take subnets from the user
        while input_subnets == "":
            input_subnets = input(
                f"\n- Enter network subnet(s) in CIDR Notation (comma-seperated) [Required]: "
            )
        # Excel file name
        workbook_name = (
            input("- Name of Excel file w/o file extension? [Default IP-Schema.xlsx]: ")
            or "IP-Schema"
        )
        # Excel sheet name
        worksheet_name = (
            input("- Worksheet name? [Default IP Schema Worksheet]: ")
            or "IP Schema Worksheet"
        )
        # Do Subnetting
        network_subnets = subnetting(input_subnets)
        # Export subnetting results to an Excel file
        export_subnets(network_subnets, workbook_name, worksheet_name)
    except KeyboardInterrupt:
        raise SystemExit(cprint("\nProcess interrupted by the user!", "yellow"))

    print("Done")


if __name__ == "__main__":
    main()
