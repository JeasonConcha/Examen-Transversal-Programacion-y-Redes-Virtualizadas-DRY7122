import netmiko
import json
from netmiko import SSHConnection

cisco1 = {
    "ip": "10.0.2.15",
    "device_type": "cisco_ios",
    "username": "netmiko",
    "password": "cisco123!"
}
command = "show version"

with SSHConnection(**cisco1) as net_connect:
    output = net_connect.send_command(command)
    print()
    print(output)
    print()
