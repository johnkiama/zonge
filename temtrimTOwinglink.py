#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:59:26 2022

@author: seismics
"""
import os

os.chdir("/home/seismics/Music/Fw _24_BIT_ZONGE_DATA")

with open("TEM22021o.avg") as fp:
    dat = fp.readlines()
    for line in dat:
        data = line.strip()
        if line.startswith(" "):
            x = (line.split()[7])
            y = float(line.split()[7])
 #           y = "%.3f" % y
#            if len(str(y)) > 5:
#                y = f'{y:.3f}'
#                y = "%.3f" % y
            y = format(y, '.3f')
          
            data = data.replace(x, str(y))
            
#            print(" " "  {} " "  {} " "  {} " "  {} " "  {}".format(x[0], x[1], x[2], str(y), x[8]))
#        print(data)
        search1 = "$ TEM: Array=INL"
        replace1_ = "$ TEM: Array=In Loop (Central Loop)"
        search2 = "$ TEM: TxRamp=150 us"
        replace2_ = "$ TEM: TXramp=150"
        search3 = "$ TEM: TxDX=300 m"
        replace3_ = "$ TEM: TXdx=300"
        search4 = "$ TEM: TxDY=300 m"
        replace4_ = "$ TEM: TXdy=300"
        search5 = "$ TEM: TxArea=90000 m^2"
        replace5_ = "$ TEM: TXarea=90000"
        search6 = "$ TEM: RxArea=10000 m^2"
        replace6_ = "$ TEM: RXarea=10000"
        search7 = "skp     Tx   Station  Freq Cmp Amps Win Time     Magnitude  RampAppRes    Depth   %Mag"
        replace7_ = "skp Tx-Coord Station  Freq Cmp Amps Win Time   Magnitude  RampAppRes    Depth     %Mag"
        search8 = "\-++-------++-------++----++-++----++-++-------++---------++---------++---------++-----+"
        replace8_ = "\-++-------++-------++----++-++----++-++-----++---------++---------++---------++-----+"
        
        data = data.replace(search1, replace1_)
        data = data.replace(search2, replace2_)
        data = data.replace(search3, replace3_)
        data = data.replace(search4, replace4_)
        data = data.replace(search5, replace5_)
        data = data.replace(search6, replace6_)
        data = data.replace(search7, replace7_)
        data = data.replace(search8, replace8_)
        
        
        
        print("", data)
        
           
        
        
        
        
        
#        print(data)
        
        
        
  #      (" " "  {} " "  {}   {}".format(x[1], x[2], float(line.split()[7])))
            
            
            
 #       with open("21942201-corrected.avg", 'w') as f:
  #          outfile = f.writelines(data)
   #         print(outfile)

