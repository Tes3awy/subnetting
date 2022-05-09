#!usr/bin/env python3
# -*- coding: utf-8 -*-

import ipaddress
from ipaddress import AddressValueError, NetmaskValueError
from typing import Any, Dict, List

from rich import print


def subnetting(input_subnets: List[Dict], gateway: int) -> List[Dict[str, Any]]:
    """Does subnetting CIDR Notation

    Parameters
    ----------
    input_subnets : List[Dict]
        Input subnets in CSV file
    gateway : int
        The selected Gateway

    Returns
    -------
    List[Dict[str, Any]]
        Result of subnetting

    Raises
    ------
    SystemExit
        AddressValueError, NetmaskValueError, ValueError, TypeError, IndexError
    """
    try:
        # Loop over input_subnets
        for subnet in input_subnets:
            cidr = ipaddress.IPv4Network(address=subnet["cidr"])

            hosts = cidr.num_addresses

            # Find range of IP addresses
            start_ip, end_ip = hosts[0], hosts[-1]

            # Output
            yield {
                "cidr": str(cidr),
                "net_addr": str(cidr.network_address),
                "prefix_len": str(cidr.prefixlen),
                "broadcast_addr": str(cidr.broadcast_address),
                "netmask": str(cidr.netmask),
                "wildcard": str(cidr.hostmask),
                "num_hosts": cidr.num_addresses,
                "range": str(start_ip)
                if start_ip == end_ip
                else f"{start_ip} → {end_ip}",
                "gateway": str(end_ip) if gateway else str(start_ip),
            }

    except (AddressValueError, NetmaskValueError, IndexError) as e:
        raise SystemExit(print(f"[red]subnetting.py: {e}")) from e
