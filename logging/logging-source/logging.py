import sys

import serial

from args_parser import ArgumentParser

def run_logger(argv):
    # Read in command line arguments
    parser = ArgumentParser()
    parser.parse(argv)
    port = parser.port

    # Open port
    s = serial.Serial(port) 

    # Begin reading data


    # Parse data


    # Either create a new file or write to an existing one
 

    # On error, attempt to reopen port








    s.close()



# if this file is called directly from the command line.
if __name__ == "__main__":
   run_logger(sys.argv[1:])
