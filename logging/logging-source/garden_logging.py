import sys

import serial

def run_logger(argv):
    # Read in command line arguments
    args_parser = argument_parser.ArgumentParser()
    args_parser.parse(argv)
    port = args_parser.port
    directory = args_parser.directory
    file_prefix = args_parser.file_prefix
    file_suffix = args_parser.file_suffix

    # Open port
    parser = data_parser.DataParser()
    reader = port_reader.PortReader(port)
    logger = data_logger.DataLogger(directory = directory, prefix = file_prefix, suffix = file_suffix)

    reader.begin()

    # Begin reading data
    while(reader.open()):
        #poll the port reader
        data_packet = reader.next_packet()
        
        measurement = parser.parse_packet(data_packet)

        logger.log(measurement)
    
    logger.close()
    print("Measurement reader ended: ", reader.get_error())
    logger.log_error(reader.get_error())


# if this file is called directly from the command line.
if __name__ == "__main__":
   run_logger(sys.argv[1:])
