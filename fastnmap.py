#!/user/bin/python3

import nmap 

fastnmap = nmap.PortScanner()

print("    ____                 __   _______")                         
print(" _/ ____\____    _______/  |_ \      \   _____ _____  ______")  
print(" \   __\\__  \  /  ___/\   __\/   |   \ /     \\__  \ \____ \ ") 
print("  |  |   / __ \_\___ \  |  | /    |    \  Y Y  \/ __ \|  |_> >")
print("  |__|  (____  /____  > |__| \____|__  /__|_|  (____  /   __/") 
print("             \/     \/               \/      \/     \/|__|")
print("Welcome to fastNmap, simple, scanning automation tool")   
print("==============================================================")
#specify IP and Type of Scan
the_ip = input("Enter the IP adress that should be scanned: ")

print("Your entered IP: ", the_ip)
type(the_ip)

outp = input("""\nEnter what type of scan should be used
                1)Full, aggressive Scan
                2)Stealth Scan, Full TCP, Service version
                3)UDP Scan \n""")
print("Your selected option is: ", outp)

#You can specify ports in scan type like: fastnmap.scan(the_ip, '1-1024' '-A -O -T4 -p-')

#OS detection, version detection, script scanning, and traceroute. All Ports, Aggressive, fast

if outp == '1':
    print("Nmap Type: ", fastnmap.nmap_version())
    fastnmap.scan(the_ip, '1-65535', '-A -O -T4 -v')                    
    print(fastnmap.scaninfo())
    print("IP State: ", fastnmap[the_ip].state())
    print(fastnmap[the_ip].all_protocols())
    print("Ports are open: ", fastnmap[the_ip]['tcp'].keys())
#Full TCP port scan using with service version detection

elif outp == '2':
    print("Nmap Type: ", fastnmap.nmap_version())
    fastnmap.scan(the_ip, '1-65535', '-sV -sS -T4 -v')
    print(fastnmap.scaninfo())
    print("IP State: ", fastnmap[the_ip].state())
    print(fastnmap[the_ip].all_protocols())
    print("Ports are open: ", fastnmap[the_ip]['tcp'].keys())
#UDP scan, show smt. false positives. Reveal Trojans running on  UDP ports/ hidden RPC services.

elif outp == '3':
    print("Nmap Type: ", fastnmap.nmap_version())
    fastnmap.scan(the_ip, '1-65535', '-v -sU')
    print(fastnmap.scaninfo())
    print("IP State: ", fastnmap[the_ip].state())
    print(fastnmap[the_ip].all_protocols())
    print("Ports are open: ", fastnmap[the_ip]['udp'].keys())
elif outp >= '4':
    print("Enter a valid option")

#this simple script will be updated and functionality will be extended

