import getopt
import sys

class ArgumentParser:
    # Arguments to parse: 
    # Port(s)
    # Baud Rate(s)
    def __init__(self):
        self.port = None
        self.file_prefix = None
        self.file_suffix = None
        self.directory = None
        self.baud_rate = None
        self.max_queue_size = None
    def parse(self, argv):
        try:
            opts,args = getopt.getopt(argv,"p:P:S:d:b:m:",["port","prefix","suffix","directory","baud_rate","max_queue_size"])
        except getopt.GetoptError:
            print("Error reading inputs. Allowable inputs are found in the README")
            sys.exit(2)
        
        # Arguments
        for opt,arg in opts:
            if opt == "-p" or opt == "--port":
                self.port = arg # or something like this
            elif opt == "-P" or opt ==  "--prefix":
                self.file_prefix = arg #or something like this
            elif opt == "-S" or opt == "--suffix":
                self.file_suffix = arg
            elif opt == "-d" or opt == "--directory":
                self.directory = arg
            elif opt == "-b" or opt == "--baud":
                self.baud_rate = arg
            elif opt == "-m" or opt == "--max_queue_size"
                self.max_queue_size = arg
    

