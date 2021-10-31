# python-ip-address-generator
Class to get any range of ips dynamically and fast

Usage:
from ipgenerator import All_ips

ips=All_ips(start_ip="172.16.0.0",end_ip="172.16.255.255")
#from 172.16.0.0 - 172.16.255.255
#or
ips=All_ips(start_ip="172.16.0.0",ip_range=100)
#from 172.16.0.0 - 172.16.0.99
ips=All_ips()
#from  0.0.0.0 - 255.255.255.255

#iterate them
for ip in ips:
  do stuff
  
#call to get the index of an ip in your range or the ip with the index
ips(index=0)
ips(ip="172.16.0.0")

#add to merge ranges
