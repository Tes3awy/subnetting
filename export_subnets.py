#!usr/bin/env python3

from datetime import date

import xlsxwriter
from termcolor import cprint


def export_subnets(
    subnets: list[dict],
    workbook_name: str = "IP-Schema",
    worksheet_name: str = "IP Schema Worksheet",
):
    """Export an Excel file of entered subnets

    Args:
        subnets (list[dict]): Processed subnets
        workbook_name (str, optional): Name of the Excel file. Defaults to "IP-Schema".
        worksheet_name (str, optional):  Name of the sheet within the Excel file. Defaults to "IP Schema Worksheet".

    Raises:
        SystemExit: TypeError
    """

    # Today's date
    today = date.today()

    excel_file_name = f"{workbook_name}_{today}.xlsx"

    # Create an Excel file
    with xlsxwriter.Workbook(excel_file_name) as workbook:
        # Create a sheet within the Excel file
        worksheet = workbook.add_worksheet(worksheet_name)
        # Filters
        worksheet.autofilter("A1:K1")
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
            "H1": "Gateway",
            "I1": "Subnet Mask",
            "J1": "Wildcard Mask",
            "K1": "Max. No. of Usable Hosts",
        }

        # Header line format
        header_line_frmt = workbook.add_format(
            {
                "bold": True,
                "border": True,
                "align": "center",
                "valign": "vcenter",
            }
        )

        # Create a header line row
        for key, value in header_line.items():
            worksheet.write_string(key, value, header_line_frmt)

        # Generic cell format
        cell_frmt = workbook.add_format(
            {
                "border": True,
                "align": "center",
                "valign": "vcenter",
            }
        )

        # Format cell containing number
        num_cell_frmt = workbook.add_format(
            {
                "border": True,
                "align": "center",
                "valign": "vcenter",
                "num_format": "#,##0",
            }
        )

        # Initial values for row and column
        row = 1
        col = 0

        try:
            # Place subnetting data according to header line above
            for net_subnet in subnets:
                worksheet.write(row, col + 0, "", cell_frmt)
                worksheet.write(row, col + 1, "", cell_frmt)
                worksheet.write(row, col + 2, net_subnet["cidr"], cell_frmt)
                worksheet.write(row, col + 3, net_subnet["net_addr"], cell_frmt)
                worksheet.write(row, col + 4, f'/{net_subnet["prefix_len"]}', cell_frmt)
                worksheet.write(row, col + 5, net_subnet["broadcast_addr"], cell_frmt)
                worksheet.write(row, col + 6, net_subnet["range"], cell_frmt)
                worksheet.write(row, col + 7, net_subnet["gateway"], cell_frmt)
                worksheet.write(row, col + 8, net_subnet["netmask"], cell_frmt)
                worksheet.write(row, col + 9, net_subnet["wildcard"], cell_frmt)
                worksheet.write_number(
                    row, col + 10, net_subnet["num_hosts"], num_cell_frmt
                )
                # Jump to next row
                row += 1

        except TypeError as e:
            raise SystemExit(cprint(e, "red"))
    cprint(f"\nPlease check {excel_file_name} in current working directory.\n", "green")
