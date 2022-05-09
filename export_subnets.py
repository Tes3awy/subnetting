#!usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from typing import Dict, List, Optional

from xlsxwriter import Workbook


def export_subnets(
    subnets: List[Dict], workbook_name: Optional[str] = "New-Schema.xlsx"
):
    """Exports an Excel file of subnetting data

    Parameters
    ----------
    subnets : List[Dict]
        List of subnets went througth subnetting
    workbook_name : Optional[AnyStr], optional
        Name of Workbook to create, by default "New-Schema.xlsx"

    Raises
    ------
    SystemExit
        TypeError, KeyError
    """

    wb_name, ext = workbook_name.split(".")
    excel_fname = f"{wb_name}_{date.today()}.{ext}"

    # Create an Excel file
    with Workbook(filename=excel_fname) as workbook:
        # Create a sheet within the Excel file
        ws = workbook.add_worksheet(name="Results")
        # Filters
        ws.autofilter("A1:L1")
        # Freeze top row and 2 most left columns
        ws.freeze_panes(1, 2)

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
        h_frmt = workbook.add_format(
            properties={
                "bold": True,
                "border": True,
                "align": "center",
                "valign": "vcenter",
            }
        )

        # Create a header line row
        for cell, str_val in header_line.items():
            ws.write(cell, str_val, cell_format=h_frmt)

        # Generic cell format
        c_frmt = workbook.add_format(
            properties={"border": True, "align": "center", "valign": "vcenter"}
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

        try:
            # Place subnetting data according to header line above
            for row, subnet in enumerate(iterable=subnets, start=2):
                ws.write(f"A{row}", "", c_frmt)
                ws.write(f"B{row}", "", c_frmt)
                ws.write(f"C{row}", subnet["cidr"], c_frmt)
                ws.write(f"D{row}", subnet["net_addr"], c_frmt)
                ws.write(f"E{row}", f'/{subnet["prefix_len"]}', c_frmt)
                ws.write(f"F{row}", subnet["broadcast_addr"], c_frmt)
                ws.write(f"G{row}", subnet["range"], c_frmt)
                ws.write(f"H{row}", "", c_frmt)
                ws.write(f"I{row}", subnet["gateway"], c_frmt)
                ws.write(f"J{row}", subnet["netmask"], c_frmt)
                ws.write(f"K{row}", subnet["wildcard"], c_frmt)
                ws.write_number(f"L{row}", int(subnet["num_hosts"]), num_frmt)

        except (TypeError, KeyError) as e:
            raise SystemExit(print(f"[red]export_subnets.py: {e}")) from e
    print(f"\n[green]Please check {excel_fname} in the PWD.", end="\n\n")
