#!/usr/bin/python3

#run by typing python3 scanner.py on terminal
#you must install the code below on terminal before running 
#pip3 install python.nmap


import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool By Stephen and Namsi")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan\n""")
print("You have selected option: ", resp)

if resp == '1':
    # -v verbose
    # -sS TCP SYN scan
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
