import socket

def print_socket_handle(sock):
    try:
        handle = sock.fileno()
        print(f"Socket handle: {handle}")
    except socket.error as e:
        print(f"Error occurred: {str(e)}")

# Example usage:
# Replace '127.0.0.1' and 8080 with the actual IP address and port number of the socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('20.56.90.62', 12345))
print_socket_handle(sock)
sock.close()