import os

class DataLogger:
    def __init__(self):
        # Easily searchable lists
        self.directory_list = []
        self.file_list = []
    
    def log(self, measurement):
        # Create a new directory if necessary
        if(not measurement.source in self.directory_list):
            self.directory_list.append(measurement.source)
            self.file_list[measurement.source] = []
            os.mkdir(measurement.source, 0o777) 
        # Create a new file if necessary
        if(not measurement.meas_type in file_list[measurement.source]):
            fh = open(measurement.source + "/" + measurement.meas_type + ".txt", "w")
            self.file_list[measurement.source].append((measurement.meas_type,fh))
        # Write to file
        fh = None
        handle_list = self.file_list[measurement.source]
        for file, handle in handle_list:
            if(file == measurement.meas_type):
                fh = handle

        if(fh):
            fh.write(measurement.time)
            fh.write(",")
            i = 0
            for v in measurement.value:
                fh.write(v)
                if(i < len(measurement.value)-1):
                    fh.write(",")
                i=i+1

    def log_error(self, source = "No Source", error = "No error"):
        if(not source in self.directory_list):
            self.directory_list.append(source)
            self.file_list[source] = []
            os.mkdir(source, 0o777) 

        filename = "runtime_errors"
        if(not filename in file_list[source]):
            fh = open(source + "/" + filename + ".txt", "w")
            self.file_list[source].append((filename,fh))
        
        fh = None
        handle_list = self.file_list[source]
        for file, handle in handle_list:
            if(file == filename):
                fh = handle

        if(fh):
            fh.write(error)

    
    def close(self):
        for source, handle_list in self.file_list:
            for file, handle in handle_list:
                handle.close()
    
        

