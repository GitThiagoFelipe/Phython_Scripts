import netmiko
from netmiko import ConnectHandler

iosv_12 = {
    "device_type": "cisco_ios",
    "ip": "10.10.100.4",
    "username": "cisco",
    "password": "cisco",
}

net_connect = ConnectHandler(**iosv_12)
#net_connect.find_prompt()
output = net_connect.send_command("sh ip int br")
print output

for n in range(2,5):
    print "Creating VLAN " + str(n)
    config_commands = ["vlan " + str(n), "name Python_VLAN " + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output

