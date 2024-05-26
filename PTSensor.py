from pymodbus.client import ModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer

# 連線設定
client = ModbusSerialClient(
    port='/dev/ttyS0',
    framer=ModbusRtuFramer,

    baudrate=9600,
    bytesize=8,
    parity="N",
    stopbits=1,
)

# 開始連線
connection = client.connect()

if  connection:

    print("connect successs!")

    try:

        res = client.read_holding_registers(
            address=1090,  # 起始地址
            count=4,  # 讀取地址數
            slave=3,
        )
        print(res.registers)
        print(res.registers[0])

    except:
        
        print("Modbus未成功連線!")

    finally:
        client.close()