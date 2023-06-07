import psutil
import socket

def print_active_socket_handles():
    connections = psutil.net_connections()
    for conn in connections:
        if conn.type == socket.SOCK_STREAM:  # Filter TCP sockets
            try:
                handle = conn.laddr[1]  # Get the local port as the socket handle
                print(f"Process ID: {conn.pid} - Local port: {handle}")
            except Exception as e:
                print(f"Error retrieving socket handle: {e}")

# Example usage:
print_active_socket_handles()