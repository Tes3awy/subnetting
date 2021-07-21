#!usr/bin/env python3

from datetime import date
from typing import AnyStr, Dict, List

from termcolor import colored, cprint
from xlsxwriter import Workbook


def export_subnets(
    subnets: List[Dict],
    workbook_name: AnyStr = "IP-Schema",
    worksheet_name: AnyStr = "IP Schema Worksheet",
):
    """Export an Excel file of entered subnets

    Args:
        subnets (List[Dict]): Processed subnets
        workbook_name (AnyStr, optional): Name of the Excel file. Defaults to "IP-Schema".
        worksheet_name (AnyStr, optional):  Name of the sheet within the Excel file. Defaults to "IP Schema Worksheet".

    Raises:
        SystemExit: TypeError
    """

    excel_fname = f"{workbook_name}_{date.today()}.xlsx"

    # Create an Excel file
    with Workbook(filename=excel_fname) as workbook:
        # Create a sheet within the Excel file
        worksheet = workbook.add_worksheet(name=worksheet_name)
        # Filters
        worksheet.autofilter("A1:L1")
        # Freeze top row and 2 most left columns
        worksheet.freeze_panes(1, 2)

        # Header line in Excel sheet
        header_line = {
            "A1": "VLAN ID",
            "B1": "VLAN Name",
            "C1": "CIDR Notation",
            "D1": "Network Address",
            "E1": "Prefix Length",
            "F1": "Broadcast Address",
            "G1": "Addresses Range",
            "H1": "IP Helper Address",
            "I1": "Gateway",
            "J1": "Subnet Mask",
            "K1": "Wildcard Mask",
            "L1": "Max. No. of Usable Hosts",
        }

        # Header line format
        header_line_frmt = workbook.add_format(
            properties={
                "bold": True,
                "border": True,
                "align": "center",
                "valign": "vcenter",
            }
        )

        # Create a header line row
        for cell, value in header_line.items():
            worksheet.write_string(cell, value, cell_format=header_line_frmt)

        # Generic cell format
        c_frmt = workbook.add_format(
            properties={
                "border": True,
                "align": "center",
                "valign": "vcenter",
            }
        )

        # Format cell containing number
        num_frmt = workbook.add_format(
            properties={
                "border": True,
                "align": "center",
                "valign": "vcenter",
                "num_format": "#,##0",
            }
        )

        # Initial values for row and column
        row, col = 1, 0

        try:
            # Place subnetting data according to header line above
            for subnet in subnets:
                worksheet.write(row, col + 0, "", c_frmt)  # A
                worksheet.write(row, col + 1, "", c_frmt)  # B
                worksheet.write(row, col + 2, subnet["cidr"], c_frmt)  # C
                worksheet.write(row, col + 3, subnet["net_addr"], c_frmt)  # D
                worksheet.write(row, col + 4, f'/{subnet["prefix_len"]}', c_frmt)  # E
                worksheet.write(row, col + 5, subnet["broadcast_addr"], c_frmt)  # F
                worksheet.write(row, col + 6, subnet["range"], c_frmt)  # G
                worksheet.write(row, col + 7, "", c_frmt)  # H
                worksheet.write(row, col + 8, subnet["gateway"], c_frmt)  # I
                worksheet.write(row, col + 9, subnet["netmask"], c_frmt)  # J
                worksheet.write(row, col + 10, subnet["wildcard"], c_frmt)  # K
                worksheet.write_number(
                    row, col + 11, subnet["num_hosts"], num_frmt
                )  # L
                # Jump to next row
                row += 1

        except TypeError as e:
            raise SystemExit(colored(f"export_subnets.py: {e}", "red"))
        except KeyError as e:
            raise SystemExit(colored(f"export_subnets.py: {e}", "red"))
    cprint(f"\nPlease check {excel_fname} in the PWD.\n", "green")
