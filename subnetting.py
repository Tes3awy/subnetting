#!usr/bin/env python3

import ipaddress
from ipaddress import AddressValueError, NetmaskValueError

from termcolor import cprint


def subnetting(input_subnets: list) -> list[dict]:
    """Does subnetting on each value entered by the user

    Args:
        input_subnets (list): Subnets entered by the user

    Raises:
        SystemExit: AddressValueError
        SystemExit: NetmaskValueError
        SystemExit: TypeError

    Returns:
        list[dict]: Result of subnetting
    """

    try:
        # Split list of network subnets
        netsubnet_list = input_subnets.split(",")
        # Define an empty list to hold the output result
        result = []
        # Loop over netsubnet_list list
        for netsubnet in netsubnet_list:
            cidr_notation = ipaddress.IPv4Network(netsubnet.strip())

            # Find range of IP addresses
            hosts = list(cidr_notation.hosts())
            start_ip = hosts[0]
            end_ip = hosts[-1]

            # Evaluate wildcard mask from netmask
            subnet_mask = str(cidr_notation.netmask).split(".")
            wildcard_mask = []
            for octet in subnet_mask:
                octet_value = 255 - int(octet)
                wildcard_mask.append(octet_value)

            wildcard_mask = ".".join(map(str, wildcard_mask))

            # Output
            # Define an empty dictionary to hold all values
            network_details = {}

            network_details["cidr"] = str(cidr_notation)
            network_details["network_address"] = str(cidr_notation.network_address)
            network_details["prefix_length"] = str(cidr_notation.prefixlen)
            network_details["broadcast_address"] = str(cidr_notation.broadcast_address)
            if start_ip == end_ip:
                network_details["range"] = f"{start_ip}"
            else:
                network_details["range"] = f"{start_ip} - {end_ip}"
            if cidr_notation.prefixlen < 32:
                network_details["gateway"] = f"{cidr_notation.network_address + 1}"
            else:
                network_details["gateway"] = str(cidr_notation.network_address)
            network_details["netmask"] = f"{cidr_notation.netmask}"
            network_details["wildcard"] = wildcard_mask
            network_details["num_hosts"] = len(hosts)

            # Add network details to network details
            result.append(network_details)

        return result

    except AddressValueError as e:
        raise SystemExit(cprint(e, "red"))
    except NetmaskValueError as e:
        raise SystemExit(cprint(e, "red"))
    except TypeError as e:
        raise SystemExit(cprint(e, "red"))
