import sys
import glob
import serial



class ChkPort():

    def __init__(self):
        """print ("Motor")"""


    def serial_ports(self):
        """Lists serial ports

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of available serial ports
        """
        #check windows
        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)]

        # Check Leenux
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this is to exclude your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')

        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')

        else:
            raise EnvironmentError('Unsupported platform')

        # List Ports
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result


def main():

    print("on Main")
    cpuertos = ChkPort()
    print("Puertos: ", cpuertos.serial_ports())


if __name__ == '__main__':
    main()
