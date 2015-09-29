import threading
import ChecaPuertos
from ChecaPuertos import ChkPort
from entrada import Serializer



class ReadingThread(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.Serial = Serializer(port)
        if self.Serial.port.isOpen() == False:
            try:
                self.Serial.open()
            except RuntimeError:
                self.PortExceptionHandler()    
    
    def PortReader(self):
        try:
            reading = self.Serial.recv()
        except RuntimeError:

            self.PortExceptionHandler()
        return reading
    
    def PortExceptionHandler(self, tries = 0):
        self.Serial.Close()
        tries =+ 1
        portRetry = [ChecaPuertos.serial_ports()]
        portRetry = portRetry[0]
        self.Serial = Serializer(portRetry)
        print'portexception'
        if self.Serial.port.isOpen() == False:
            try:
                self.Serial.open()
            except RuntimeError:
                if tries > 3:
                    return
                else:
                    self.PortExceptionHandler(tries)
        
        
   
def main():
    cps = ChkPort()
    newport = cps.serial_ports()
    #newport = ChecaPuertos.serial_ports()
    newPort = newport[0]
    reader = ReadingThread(newPort)
    while True:
        printVal = reader.PortReader()
        print (printVal)
        
if __name__ == "__main__":
    main()