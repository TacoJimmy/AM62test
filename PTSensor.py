
import codecs
# -*- coding: UTF-8 -*-


from pymodbus.client import ModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer
import time



mod_client = ModbusSerialClient(
    port='/dev/ttyS3',
    framer=ModbusRtuFramer,

    baudrate=19200,
    bytesize=8,
    parity="N",
    stopbits=1,
)
# 開始連線
connection = mod_client.connect()




EC01_Temp = mod_client.read_holding_registers(address=0,count=1,slave=2)
    
print("EC01_Temp_Data = ", EC01_Temp.registers)