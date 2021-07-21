#!usr/bin/env python3

import csv
from typing import AnyStr, List


def read_subnets(file_path: AnyStr = "subnets.csv") -> List[List]:
    """Read CSV subnets file

    Args:
        file_path (AnyStr, optional): Path to subnets CSV file. Defaults to "subnets.csv".

    Returns:
        List[List]: Subnets in CIDR notation representation
    """
    # Define an empty list to hold all subnets
    subnets = []

    # Read subnets CSV file
    with open(file=file_path, mode="r") as csvfile:
        next(csvfile)  # Skip header line
        csv_data = csv.reader(
            csvfile, delimiter="\n", dialect="excel", doublequote=True
        )
        for subnet in csv_data:
            subnets.append(subnet[0])

    return subnets
