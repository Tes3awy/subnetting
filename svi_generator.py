#!usr/bin/env python3

import os
from datetime import datetime
from typing import AnyStr

import pandas as pd
from jinja2 import Environment, FileSystemLoader


def svi_generator(excel_file: AnyStr) -> None:
    """Generates an SVI configuration template

    Args:
        excel_file (AnyStr): Path to the Excel file
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
        io=os.path.join("./", excel_file), sheet_name=0, usecols="A:B,H:I"
    )
    df = pd.DataFrame(data=data)

    # Create a vlans dictionary from columns
    vlans = df.rename(
        columns={
            "VLAN ID": "id",
            "VLAN Name": "name",
            "Gateway": "ipaddr",
            "Subnet Mask": "mask",
        }
    ).to_dict(orient="records")

    # Render the templpate
    svi_cfg = template.render(vlans=vlans)

    # Export the template result to a text file
    cfg_fname = f'{excel_file.replace(".xlsx", "")}_svi_template.txt'
    with open(file=cfg_fname, mode="w", encoding="utf-8") as cfg_file:
        cfg_file.write(svi_cfg.lstrip())
