from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

#Define the target to use when setting the ip destination
target = "www.target.com/30"
#Inputs the source and deastination for the ip
ip = IP(dst=target)
print(ip)

#constructing a basic network packet that
# includes both an Ethernet frame and an IP packet, each with default headers
my_frame = Ether()/IP()

#Capturing and assigning 50 packets to the p variable with the sniff method
p = sniff(count=50)
#Plotting the length of the 50 packets using matplotlib .plot method
#Using lambda to teake the length of each packet before ploting it
#x is just a variable name used to represent each individual packet per iteration
p.plot(lambda x: len(x))



#Since its a list of packets you will need to loop through it or use index notation to access the packets contents
for packets in p:
    print(packets)

print("This is the captured packets: ")
#print(p)

#Prints out breif info on the collected packets
p.summary()

#Class Notes:
#Target specific companies as your potential clients
#language model with no filter (Open source)