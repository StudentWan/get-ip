import os
import re
import time

def getIp():
	ip = []
	ipconfig = os.popen('ifconfig')
	pattern = re.compile('(.*?)(\d+\.\d+\.\d+\.\d+)')

	for eachLine in ipconfig:
		ipv4Line = re.search(pattern,eachLine)
		if ipv4Line is not None:
			ipv4 = ipv4Line.groups()
			ip.append(ipv4[1])

	return ip

print "getting 10_ip ..."
currentIp = getIp()
print "current ip is: "+currentIp[1]


os.popen("sudo ipconfig set en0 DHCP")
time.sleep(4)
currentIp = getIp()

while currentIp[1].startswith('10.109')!=1:
	print 'still not correct ip, plz wait...'
	os.popen("sudo ipconfig set en0 DHCP")
	time.sleep(4)
	currentIp = getIp()

print "Now currentIp is: "+currentIp[1]