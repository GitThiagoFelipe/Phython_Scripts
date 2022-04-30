import getpass
import sys
import telnetlib

user = input("Entre com seu usuário: ")
password = getpass.getpass()
IP_Switches = open("IP_Switches")

for EachSwitche in IP_Switches:
    print("Configurando Switch " + str(EachSwitche) + "\n")
    tn = telnetlib.Telnet(EachSwitche)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"config t\n")

    for n_vlans in range(2,51):
        tn.write(b"vlan " + str(n_vlans).encode("ascii") + b"\n")
        tn.write(b"name Phyton_VLAN_" + str(n_vlans).encode("ascii") + b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode("ascii"))