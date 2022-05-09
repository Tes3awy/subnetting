#!usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from typing import Dict, List


def read_subnets(file_path: str = "subnets.csv") -> List[Dict[str, str]]:
    """Reads CSV subnets file

    Parameters
    ----------
    file_path : str, optional
        Name of a CSV file, by default "subnets.csv"

    Returns
    -------
    List[Dict[str, str]]
        Subnets in CIDR Notation
    """

    # Read subnets CSV file
    with open(file=file_path, mode="rt", encoding="utf-8") as csvfile:
        next(csvfile)  # Skip header line
        csv_data = csv.DictReader(f=csvfile, fieldnames={"cidr"})
        return list(csv_data)
