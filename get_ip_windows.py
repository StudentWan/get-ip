import os
import re

def getIp():
	ip = []
	ipconfig = os.popen('ipconfig')
	pattern = re.compile('(.*?)(\d+\.\d+\.\d+\.\d+)')

	for eachLine in ipconfig:
		ipv4Line = re.search(pattern,eachLine)
		if ipv4Line is not None:
			ipv4 = ipv4Line.groups()
			ip.append(ipv4[1])

	print "currentIp is: " + ip[0]
	return ip

print "getting 10_ip ..."
counter = 0
currentIp = getIp()

while ((currentIp[1] != '255.255.252.0') or (currentIp[2] !='10.109.32.1')):
	os.popen("ipconfig /release")
	os.popen("ipconfig /renew")
	counter += 1
	currentIp = getIp()

print str(counter)+" OK! your courrent ip is: "+currentIp[0]