import getpass
import sys
import telnetlib

host = "10.10.100.2"
user = input("Entre com seu usuário: ")
password = getpass.getpass()
tn = telnetlib.Telnet(host)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("config t\n")
tn.write("int lo0\n")
tn.write("ip add 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print
tn.read_all()



