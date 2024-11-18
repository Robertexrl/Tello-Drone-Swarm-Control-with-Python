# Tello Drone Swarm Control with Python
This repository provides a Python script to control multiple Tello drones in swarm mode. The code enables simultaneous execution of commands such as "takeoff," "move up," "rotate," and "land" across a fleet of drones using UDP communication.

Features
Control multiple Tello drones concurrently.
Execute synchronized flight commands including takeoff, movement, rotation, and landing.
Customizable drone fleet by modifying the IP addresses in the code.
Real-time feedback from each drone via a background thread.
Prerequisites
Python Installation: Ensure Python 3 is installed.
Network Setup: Connect all Tello drones to their respective Wi-Fi networks and note their IP addresses.
Python Libraries: No additional installations are required as the script uses built-in libraries (socket, threading, and time).
How to Use
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/tello-swarm-control.git
cd tello-swarm-control
Edit the tello_addresses list in the script to include the IP addresses of your drones:

python
Copy code
tello_addresses = [
    ('192.168.10.1', 8889),
    ('192.168.10.2', 8889),
    ('192.168.10.3', 8889)
]
Run the script:

bash
Copy code
python tello_swarm_control.py
Watch as your drones execute the synchronized commands.

Notes
Ensure that all drones are powered on and connected to the correct networks before running the script.
Commands are sent via UDP, so all drones must be reachable on the specified IP addresses.
Extend the script by adding new commands or complex flight paths for advanced swarm behaviours.
Disclaimer
This script is designed for educational purposes. Always follow safety guidelines and operate drones in safe environments.

# Connecting Multiple Drones
To control multiple Tello drones from one laptop, follow these steps:

1. Use a Router or Access Point
Set up a router or a mobile hotspot to act as the central Wi-Fi network.
Connect all drones to this router or hotspot.
Connect your laptop to the same network.
2. Assign Unique IP Addresses
By default, drones should automatically receive unique IP addresses from the router using DHCP (Dynamic Host Configuration Protocol).
You can verify the IPs by checking the connected devices list on the router.
3. Modify Your Script
Update the tello_addresses list in your script to include the IP addresses assigned to each drone by the router. For example:
python
Copy code
tello_addresses = [
    ('192.168.10.2', 8889),  # Drone 1
    ('192.168.10.3', 8889),  # Drone 2
    ('192.168.10.4', 8889)   # Drone 3
]
Why Use a Router?
Direct Wi-Fi Limitations: Laptops can only connect to one Wi-Fi network at a time. Without a router, you would need multiple network interfaces (e.g., external USB Wi-Fi adapters) to connect directly to multiple drones, which is cumbersome.
Network Management: A router or access point provides a single network for all drones and your laptop, simplifying communication.
Practical Considerations
Router Distance and Range: Ensure the router or access point has enough range to cover all drones in the swarm.
Network Congestion: Limit the number of devices on the network to avoid interference.
UDP Ports: Each drone listens for commands on port 8889. Ensure these ports are not blocked by firewalls or network configurations.
Drone Firmware: Ensure all drones have the latest firmware for stable operation in swarm mode.
Example Setup
Router SSID: TelloSwarm
Laptop IP: 192.168.10.100
Drone IPs:
Drone 1: 192.168.10.2
Drone 2: 192.168.10.3
Drone 3: 192.168.10.4
In this setup, the laptop communicates with all drones through the router, and the script sends commands to their respective IP addresses.
