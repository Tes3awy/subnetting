#!usr/bin/env python3

import csv


def read_subnets(file_path: str = "subnets.csv") -> list[list]:
    """Read CSV subnets file

    Args:
        file_path (str, optional): Path to subnets CSV file. Defaults to "subnets.csv".

    Returns:
        list[list]: Subnets in CIDR notation representation
    """
    # Define an empty list to hold all subnets
    subnets = []
    # Read subnets CSV file
    with open(file=file_path, mode="r") as csvfile:
        next(csvfile)  # Skip header line
        csv_data = csv.reader(csvfile, delimiter=",")

        for subnet in csv_data:
            subnets.append(subnet)

    return subnets
