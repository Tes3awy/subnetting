#!usr/bin/env python3
# -*- coding: utf-8 -*-

from ipaddress import AddressValueError, IPv4Network, NetmaskValueError
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
        AddressValueError, NetmaskValueError, IndexError
    """
    try:
        # Loop over input_subnets
        for subnet in input_subnets:
            network = IPv4Network(address=subnet["cidr"])

            hosts = list(network.hosts())

            yield {
                "cidr": str(network),
                "net_addr": str(network.network_address),
                "prfx_len": str(network.prefixlen),
                "brdcst_addr": str(network.broadcast_address),
                "netmask": str(network.netmask),
                "wildmask": str(network.hostmask),
                "num_hosts": network.num_addresses - 2,
                "range": str(hosts[0])
                if hosts[0] == hosts[-1]
                else f"{hosts[0]} → {hosts[-1]}",
                "gateway": str(hosts[0]) if gateway else str(hosts[-1]),
            }

    except (AddressValueError, NetmaskValueError, IndexError) as e:
        raise SystemExit(print(f"[red]subnetting.py: {e}")) from e
