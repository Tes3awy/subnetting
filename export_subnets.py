#!usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from typing import Dict, Generator, List, Optional

from rich import print
from xlsxwriter import Workbook


def export_subnets(
    subnets: Generator, workbook_name: Optional[str] = "New-Schema.xlsx"
):
    """Exports an Excel file of subnetting data

    Parameters
    ----------
    subnets : Generator
        subnets went througth subnetting
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
    with Workbook(filename=excel_fname) as wb:
        # Create a sheet within the Excel file
        ws = wb.add_worksheet(name="Results")
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
            "L1": "Max. Usable Hosts",
        }

        # Header line format
        h_frmt = wb.add_format(
            properties={
                "bold": True,
                "border": True,
                "align": "center",
                "valign": "vcenter",
            }
        )

        # Create a header line row
        for cell, str_val in header_line.items():
            ws.write_string(cell, str_val, cell_format=h_frmt)

        # Generic cell format
        c_frmt = wb.add_format(
            properties={"border": True, "align": "center", "valign": "vcenter"}
        )

        # Format cell containing number
        num_frmt = wb.add_format(
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
                ws.write(f"E{row}", f'/{subnet["prfx_len"]}', c_frmt)
                ws.write(f"F{row}", subnet["brdcst_addr"], c_frmt)
                ws.write(f"G{row}", subnet["range"], c_frmt)
                ws.write(f"H{row}", "", c_frmt)
                ws.write(f"I{row}", subnet["gateway"], c_frmt)
                ws.write(f"J{row}", subnet["netmask"], c_frmt)
                ws.write(f"K{row}", subnet["wildmask"], c_frmt)
                ws.write_number(f"L{row}", subnet["num_hosts"], num_frmt)

        except (TypeError, KeyError) as e:
            raise SystemExit(print(f"[red]export_subnets.py: {e}")) from e
    print(f"\n[green]Please check {wb.filename} in the cwd.", end="\n\n")
