#!usr/bin/env python3

from colorama import init

from export_subnets import export_subnets
from subnetting import subnetting

init(autoreset=True)


def main():
    # Take inputs from the user
    input_subnets = input(
        "\n- Enter network subnet(s) in CIDR Notation (comma-seperated): "
    )
    workbook_name = (
        input("- Name of Excel file w/o file extension? [Default IP-Schema.xlsx]: ")
        or "IP-Schema"
    )
    worksheet_name = (
        input("- Worksheet name? [Default IP Schema]: ") or "IP Schema Worksheet"
    )

    # Do Subnetting
    network_subnets = subnetting(input_subnets)

    # Export subnetting results to an Excel file
    export_subnets(network_subnets, workbook_name, worksheet_name)

    print("Done")


if __name__ == "__main__":
    main()
