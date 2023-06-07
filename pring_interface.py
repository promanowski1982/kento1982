import psutil
import socket

network_interfaces = psutil.net_if_addrs()
for interface, addresses in network_interfaces.items():
    print(f"Interface: {interface}")
    for address in addresses:
        if address.family == socket.AF_INET:
            print(f"  IP Address: {address.address}")