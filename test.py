from netaddr import IPNetwork, IPAddress, AddrFormatError
import os
from collections import defaultdict

no_op = 0
score = defaultdict(int)

def loadDict(fname):
    with open(fname) as f:
        content = f.readlines()
        return content

def convertToNewDict(fname):
    with open(fname) as f:
        ipNetworks = f.readlines()
        a = []
        for ipNetwork in ipNetworks:
            ip_network = ipNetwork.strip('\n')
            start = IPNetwork(ip_network).first
            end = IPNetwork(ip_network).last
            a.append([ip_network, start, end])
        return a

def inMask2(queryIp, newDict):
    qip0 = queryIp.strip('\n')
    qip = IPAddress(qip0).value
    for element in newDict:
        ipnetwork = element[0]
        start = element[1]
        end = element[2]
        if (qip >= start):
            if (qip <= end):
                print qip0 + " is in " + ipnetwork
                makeScore2(ipnetwork)

def makeScore(key):
    global score
    if not key in score:
        score[key] = 1
    else:
        score[key] += 1
    return score

def makeScore2(key):
    global score
    score[key] += 1

def processIp2(fname, dict):
    with open(fname) as e:
        ips = e.readlines()
        for ip in ips:
            inMask2(ip, dict)

def processIp3(fname, dict):
    with open(fname) as e:
        for ip in e:
            try:
                inMask2(ip, dict)
            except  AddrFormatError:
                no_op
            else:
                no_op


newdict = convertToNewDict(os.getcwd() + "/dict.txt")
processIp3(os.getcwd() + "/111.txt", newdict)

print score.items()

print "done"