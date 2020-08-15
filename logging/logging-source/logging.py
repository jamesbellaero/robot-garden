import sys, getopt

import serial

def run_logger(argv):
    # Read in command line arguments
    try:
        opts,args = getopt.getopt(argv,"i:j:",["opt1","opt2"])
    except getopt.GetoptError:
        print 'Error reading inputs. Allowable inputs are found in the README'
        sys.exit(2)
    
    for opt,arg in opts:
        if opt == "-i","--opt1":
            port = arg # or something like this
        elif opt == "-j","--opt2":
            outfile = arg #or something like this
            
    # Open port
    s = serial.Serial('/dev/ttyUSB0') 

    # Begin reading data


    # Parse data


    # Either create a new file or write to an existing one


    # On error, attempt to reopen port








    ser.close()















# if this file is called directly from the command line.
if __name__ == "__main__":
   run_logger(sys.argv[1:])
