import getopt

class ArgumentParser:
    # Arguments to parse: 
    # Port(s)
    # Baud Rate(s)
    def __init__(self):
        self.port = None
        self.file_prefix = None
        self.file_suffix = None
        self.directory = None
    def parse(self, argv):
        try:
            opts,args = getopt.getopt(argv,"i:j:",["opt1","opt2"])
        except getopt.GetoptError:
            print 'Error reading inputs. Allowable inputs are found in the README'
            sys.exit(2)
        
        # Arguments
        for opt,arg in opts:
            if opt == "-i","--opt1":
                port = arg # or something like this
            elif opt == "-j","--122opt2":
                outfile = arg #or something like this

