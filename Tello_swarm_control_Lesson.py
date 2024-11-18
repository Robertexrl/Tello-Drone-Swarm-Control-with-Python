
# Tello Drone Swarm Control Script with Detailed Explanation
# This script demonstrates how to control multiple Tello drones in swarm mode using Python.

# Import the necessary modules
import socket
import threading
import time

# Explanation of IP Addresses and Setup:
# Each Tello drone has a default IP address of 192.168.10.1 when connected directly.
# To control multiple drones, use a router or mobile hotspot to connect all drones and your laptop to the same network.
# The router assigns unique IP addresses to each drone, such as 192.168.10.2, 192.168.10.3, etc.
# Update the list below with the actual IP addresses assigned to your drones.

# Define the IP and port for each Tello in the swarm
tello_addresses = [
    ('192.168.10.2', 8889),  # Replace with the actual IPs of your drones
    ('192.168.10.3', 8889),
    ('192.168.10.4', 8889)
]

# IP and port of the local computer (laptop)
local_address = ('', 9000)

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)

# Send the message to all Tello drones and allow for a delay in seconds
def send_to_all(message, delay):
    for address in tello_addresses:
        try:
            sock.sendto(message.encode(), address)
            print(f"Sending '{message}' to {address}")
        except Exception as e:
            print(f"Error sending to {address}: {e}")
    time.sleep(delay)

# Receive messages from Tello drones
def receive():
    while True:
        try:
            response, ip_address = sock.recvfrom(128)
            print(f"Received from {ip_address}: {response.decode('utf-8')}")
        except Exception as e:
            print(f"Error receiving: {e}")
            break

# Start a background thread to listen for responses
receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

# Example Flight Commands for the Swarm
# Step 1: Put all Tello drones into command mode
send_to_all("command", 3)

# Step 2: Take off all drones
send_to_all("takeoff", 5)

# Step 3: Go up by 100 cm
send_to_all("up 100", 4)

# Step 4: Perform a 360-degree clockwise yaw
send_to_all("cw 360", 5)

# Step 5: Land all drones
send_to_all("land", 5)

print("Mission completed successfully!")

# Close the socket
sock.close()
