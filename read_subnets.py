#!usr/bin/env python3

import csv
from typing import AnyStr, Dict, List


def read_subnets(file_path: AnyStr = "subnets.csv") -> List[Dict[AnyStr, AnyStr]]:
    """Reads CSV subnets file

    Parameters
    ----------
    file_path : AnyStr, optional
        Name of a CSV file, by default "subnets.csv"

    Returns
    -------
    List[Dict[AnyStr, AnyStr]]
        Subnets in CIDR Notation
    """

    # Read subnets CSV file
    with open(file=file_path, mode="r") as csvfile:
        next(csvfile)  # Skip header line
        csv_data = csv.DictReader(f=csvfile, fieldnames={"cidr"})
        return [cidr for cidr in csv_data]
