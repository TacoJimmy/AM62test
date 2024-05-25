'''
Created on 2024年5月14日

@author: Jimmy
'''

import codecs
# -*- coding: UTF-8 -*-

 
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time


master = modbus_rtu.RtuMaster(serial.Serial(port='COM3', baudrate=9600, bytesize=8, parity="N", stopbits=1, xonxoff=0))
master.set_timeout(5.0)
master.set_verbose(True)


if __name__ == '__main__':
    
    while True:
        TH_Sensor = master.execute(3, cst.READ_HOLDING_REGISTERS, 1090, 4)
        Temp = round(TH_Sensor[0] * 0.01,1)
        Humd = round(TH_Sensor[3] * 0.01,1)
        time.sleep(0.01)
        
        
        print (Temp)
        print (Humd)

        
        time.sleep(5)
    
    