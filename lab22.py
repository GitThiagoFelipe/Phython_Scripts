import getpass
import sys
import telnetlib

host = "10.10.100.2"
user = input("Entre com seu usuário: ")
password = getpass.getpass()
tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn(password.encode("ascii") + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"config t\n")
tn.write(b"int lo0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))



