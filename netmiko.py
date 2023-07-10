import netmiko  
import json
from netmiko import connecthandler

cisco1 = {
    "ip": "10.0.2.15",
    "device_type": "cisco_ios",
    "username": "netmiko",
    "password":"cisco123!"
}
# show command that we execute.
command = "show version"
with connecthandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)
    #autmaticallly cleans up the output so that show output is returned
    print()
    print(output)
    print()
