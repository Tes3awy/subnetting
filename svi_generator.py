#!usr/bin/env python3

import os
from datetime import date, datetime

import pandas as pd
from jinja2 import Environment, FileSystemLoader


def svi_generator(excel_file: str):
    """Generate an SVI configuration template

    Args:
        excel_file (str): Path to the Excel file
    """

    today = date.today()

    # Handle Jinja template
    env = Environment(
        loader=FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template(os.path.join("./", "svi.j2"))
    template.globals["now"] = datetime.now

    # Read the Excel file
    data = pd.read_excel(os.path.join("./", excel_file), usecols="A:B,H:I")
    df = pd.DataFrame(data)

    # Create a vlans dictionary from columns
    vlans = {
        "vlans": df.rename(
            columns={
                "VLAN ID": "id",
                "VLAN Name": "name",
                "Gateway": "ipaddr",
                "Subnet Mask": "mask",
            }
        ).to_dict(orient="records")
    }

    # Render the templpate
    cfg = template.render(vlans)

    # Export the template result to a text file
    with open(
        file=f'{excel_file.replace(".xlsx", "")}_svi_template_{today}.txt',
        mode="w",
        encoding="UTF-8",
    ) as cfg_file:
        cfg_file.write(cfg)
