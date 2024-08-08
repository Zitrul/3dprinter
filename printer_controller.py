import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import serial
from past.builtins import raw_input
#import serial.tools.list_ports

#ports = serial.tools.list_ports.comports()

#for port in ports:
#    print(port)
def print_file(filename, port, baud):
    gcode_file = open(filename)
    gcode = gcode_file.readlines()
    gcode_file.close()
    ser = serial.Serial(port, baud)
    time.sleep(1)

    colorama_init()
    for i in gcode:
        if ";" not in i and i != "":
            print(f"{Fore.GREEN} + {i}")
            ser.write(i.encode())
            try:
                response = ser.readline().decode().strip()

                print(f"{Fore.RED} + {response}")
            except:
                print("ERR")
            while response.lower() != "ok":
                try:
                    response = ser.readline().decode().strip()
                    print(f"{Fore.YELLOW} + {response}")

                except:
                    print("ERR")
    print(f"{filename} printed")
    return


