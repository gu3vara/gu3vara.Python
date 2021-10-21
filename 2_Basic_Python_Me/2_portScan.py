#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:M3rrio,time:2021/10/21

from scapy.all import *

conf.verb = 0

tgt = input("target is : ")
sPort = input("start port is: ")
ePort = input("end port is: ")

for dPort in range(int(sPort),int(ePort)):

    pkt = IP(dst=tgt) / TCP(dport=dPort)
    ans,uans = sr(pkt)
    res = str(ans[0])

    if re.findall("SA",res):
        print(str(dPort) + "   is Open!!  ")
    else:
        pass

