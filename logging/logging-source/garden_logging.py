import sys

import serial

from args_parser import ArgumentParser
from logger import Logger

def run_logger(argv):
    # Read in command line arguments
    parser = ArgumentParser()
    parser.parse(argv)
    port = parser.port
    directory = parser.directory
    file_prefix = parser.file_prefix
    file_suffix = parser.file_suffix

    # Open port
    

    # Begin reading data
    #poll the port reader
    
    # Parse data
    #pass the data to the data parser


    # Either create a new file or write to an existing one
    #pass the results to the logger
 

    # On error, attempt to reopen port








    



# if this file is called directly from the command line.
if __name__ == "__main__":
   run_logger(sys.argv[1:])
