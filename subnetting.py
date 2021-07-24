#!usr/bin/env python3

import ipaddress
from ipaddress import AddressValueError, NetmaskValueError
from typing import Any, AnyStr, Dict, List

from termcolor import colored


def subnetting(input_subnets: List[Dict], gateway: int) -> List[Dict[AnyStr, Any]]:
    """Does subnetting CIDR Notation

    Parameters
    ----------
    input_subnets : List[Dict]
        Input subnets in CSV file
    gateway : int
        The selected Gateway

    Returns
    -------
    List[Dict[AnyStr, Any]]
        Result of subnetting

    Raises
    ------
    SystemExit
        AddressValueError, NetmaskValueError, ValueError, TypeError, IndexError
    """
    try:
        # Empty list to hold all subnetting values
        results = []
        # Loop over input_subnets
        for subnet in input_subnets:
            cidr = ipaddress.IPv4Network(subnet["cidr"])

            # Find range of IP addresses
            hosts = list(cidr.hosts())
            start_ip, end_ip = hosts[0], hosts[-1]

            # Evaluate wildcard mask from netmask
            subnet_mask = str(cidr.netmask).split(".")
            wildcard_mask = [255 - int(octet) for octet in subnet_mask]
            wildcard_mask = ".".join(map(str, wildcard_mask))

            # Output
            network_details = {
                "cidr": str(cidr),
                "net_addr": str(cidr.network_address),
                "prefix_len": str(cidr.prefixlen),
                "broadcast_addr": str(cidr.broadcast_address),
                "netmask": str(cidr.netmask),
                "wildcard": wildcard_mask,
                "num_hosts": len(hosts),
                "range": str(start_ip)
                if start_ip == end_ip
                else f"{start_ip} → {end_ip}",
                "gateway": str(end_ip) if gateway else str(start_ip),
            }

            results.append(network_details)

        return results

    except (
        AddressValueError,
        NetmaskValueError,
        ValueError,
        TypeError,
        IndexError,
    ) as e:
        raise SystemExit(colored(f"subnetting.py: {e}", "red"))
