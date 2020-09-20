import serial
import time
ser = serial.Serial(
    port='/dev/ttyS0',\
    baudrate=57600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
message = 'x,y,z,end' 
while True:
    message = ser.readline()
    data = message.split(",")
    if len(data) != 4:
	continue
#    print(data)
    print("x=" + data[0] + " y=" + data[1] + " z=" + data[2])
    time.sleep(0.5);
ser.close()
