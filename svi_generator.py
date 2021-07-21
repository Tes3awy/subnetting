#!usr/bin/env python3

import os
from datetime import date, datetime
from typing import AnyStr

import pandas as pd
from jinja2 import Environment, FileSystemLoader


def svi_generator(excel_file: AnyStr) -> None:
    """Generate an SVI configuration template

    Args:
        excel_file (AnyStr): Path to the Excel file
    """

    today = date.today()

    # Handle Jinja template
    env = Environment(
        loader=FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template(
        name=os.path.join("./", "svi.j2"),
        globals={"now": datetime.now().replace(microsecond=0)},
    )

    # Read the Excel file
    data = pd.read_excel(io=os.path.join("./", excel_file), usecols="A:B,H:I")
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
    with open(
        file=f'{excel_file.replace(".xlsx", "")}_svi_template.txt', mode="w"
    ) as cfg_file:
        cfg_file.write(svi_cfg.lstrip())
