
import serial
from ChecaPuertos import ChkPort



#configure the serial connections (the parameters differs on the device you are connecting to)

class Serializer:

    def __init__(self, port, baudrate=9600, timeout=.1): 
        self.port = serial.Serial(port = port, baudrate=baudrate, 
        timeout=timeout, writeTimeout=timeout)
 
    def open(self): 
        ''' Abre Puerto Serial'''
        print("Puerto abierto")
        self.port.open()
 
    def close(self): 
        ''' Cierra Puerto Serial'''
        self.port.close() 
     
    def send(self, msg):

        self.port.write(msg)
 
    def recv(self):
        ''' lee salidas del dispositivo serial '''
        #print("leyendo")

        return self.port.readline()

PORT = '/dev/ttyUSB0' #Esto puede necesitar cambiarse


# test main class made for testing
def main():
    cps = ChkPort()
    newport = cps.serial_ports()
    #newport = ChecaPuertos.serial_ports()
    newPort = newport[0]
    test_port = Serializer(port = newPort)
        
    while True:
        print(test_port.recv())

if __name__ == "__main__":
    main()