import sys

import serial

import port_reader
import data_logger
import data_parser
import port_reader
import argument_parser

def run_logger(argv):
    # Read in command line arguments
    args_parser = argument_parser.ArgumentParser()
    args_parser.parse(argv)
    port = args_parser.port
    directory = args_parser.directory
    file_prefix = args_parser.file_prefix
    file_suffix = args_parser.file_suffix
    baud_rate = args_parser.baud_rate
    max_queue_size = args_parser.max_queue

    # Open port
    parser = data_parser.DataParser()

    reader_kwargs = dict(port = port,baud_rate = baud_rate, max_size = max_queue_size)
    reader = port_reader.PortReader(**{k: v for k, v in reader_kwargs.items() if v is not None})

    logger_kwargs = dict(directory = directory, prefix = file_prefix, suffix = file_suffix)
    logger = data_logger.DataLogger() #**{k: v for k, v in logger_kwargs.items() if v is not None}

    reader.start()

    # Begin reading data
    while(reader.is_alive()):
        #poll the port reader
        data_packet = reader.next_packet()

        if(not data_packet):
            continue
        
        measurement = parser.parse_packet(data_packet)

        logger.log(measurement)
    
    
    logger.close()

    error_list = reader.get_errors()
    print("Measurement reader ended: ", error_list[len(error_list)-1])
    for err in error_list:
        logger.log_error(source = "PortReader", error = err)
    for err in parser.get_errors():
        logger.log_error(source = "DataParser", error = err)
    for err in logger.get_errors():
        logger.log_error(source = "DataLogger", error = err)


# if this file is called directly from the command line.
if __name__ == "__main__":
   run_logger(sys.argv[1:])
