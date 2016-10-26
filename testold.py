from netaddr import IPNetwork, IPAddress
import os
#if IPAddress("192.168.0.1") in IPNetwork("192.168.0.0/24"):
#    print "in it!"
#ipRange = ["192.168.0.0/24","192.168.0.0/25"]


def loadDict(fname):
    with open(fname) as f:
        content = f.readlines()
        return content


def inMask(queryIp, ipRange):
    for range in ipRange:
        #print range
        if IPAddress(queryIp) in IPNetwork(range):
            print "ip " + queryIp + " in range: " + range



print "start load dict"
dict = loadDict(os.getcwd() + "/dict.txt")
print "load dict done"
#inMask("223.27.116.10", dict)

print "---------------\n"



def processIp(fname):
    with open(fname) as e:
        ips = e.readlines()
        for ip in ips:
            ip = ip.strip('\n')
            inMask(ip, dict)


processIp(os.getcwd() + "/111.txt")
