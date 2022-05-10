#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime

import pandas as pd
from jinja2 import Environment, FileSystemLoader
from rich import print


def svi_generator(excel_file: str) -> None:
    """Generates an SVI configuration template

    Parameters
    ----------
    excel_file : AnyStr
        Name of an Excel file
    """

    # Handle Jinja template
    env = Environment(
        loader=FileSystemLoader(searchpath="./"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template(
        name=os.path.join("./", "svi.j2"),
        globals={"now": datetime.now().replace(microsecond=0)},
    )

    # Read the Excel file
    data = pd.read_excel(
        io=os.path.join("./", excel_file), sheet_name=0, usecols="A:B,H:J"
    )

    vlans = (
        pd.DataFrame(data=data)
        .fillna(value="")
        .drop_duplicates(subset=[data.columns[0]])
        .rename(
            columns={
                "VLAN ID": "id",
                "VLAN Name": "name",
                "Gateway": "ip",
                "Subnet Mask": "mask",
                "IP Helper Address": "helper_addr",
            }
        )
        .to_dict(orient="records")
    )

    # Render the templpate
    svi_cfg = template.render(vlans=vlans)

    # Export the template result to a text file
    cfg_fname = f'{excel_file.replace(".xlsx", "")}_SVI-template.txt'
    with open(file=cfg_fname, mode="wt+", encoding="utf-8") as f:
        f.write(svi_cfg)

    return f
