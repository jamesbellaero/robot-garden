import os

class DataLogger:
    def init(self):
        # Easily searchable lists
        self.directory_list = []
        self.file_list = []
    
    def log(self, measurement):
        # Create a new directory if necessary
        if(not directory_list.contains(measurement.source)):
            self.directory_list.append(measurement.source)
            self.file_list[measurement.source] = []
            os.mkdir(measurement.source, 0o777) 
        # Create a new file if necessary
        if(not file_list[measurement.source].contains(measurement.meas_type)):
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
        
        

