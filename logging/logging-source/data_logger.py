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
            self.file_list.append({"source" : measurement.source, "files" : []})
            if(not os.path.isdir(measurement.source)):
                os.mkdir(measurement.source, 0o777) 

        
        # Create a new file if necessary
        source_dict = next((s for s in self.file_list if s["source"] == measurement.source),None)
        meas_dict = next((s for s in source_dict["files"] if s["meas_type"] == measurement.meas_type),None)
        
        if(not meas_dict):
            fh = open(measurement.source + "/" + measurement.meas_type + ".txt", "w")
            fh.write("Time (s), ")
            fh.write(str(measurement.units))
            fh.write("\n")
            meas_dict = {"meas_type" : measurement.meas_type, "file_handle" : fh}
            source_dict["files"].append(meas_dict)
        
        
        # Write to file
        fh = meas_dict["file_handle"]
        if(fh):
            fh.write(str(measurement.time))
            fh.write(",")
            fh.write(str(measurement.value))
            fh.write("\n")
            fh.flush()
        
        else:
            print("Could not find file handle for ", measurement.source, " - ", measurement.meas_type)
            print(str(fh))

            # *** In case values can be lists, fix this to not error ***
            # i = 0
            # for v in measurement.value:
            #     fh.write(str(v))
            #     if(i < len(measurement.value)-1):
            #         fh.write(",")
            #     i=i+1

    def log_error(self, source = "No Source", error = "No error"):
        if(not source in self.directory_list):
            self.directory_list.append(source)
            self.file_list.append({"source" : source, "files" : []})
            if(not os.path.isdir(source)):
                os.mkdir(source, 0o777) 

        filename = "runtime_errors"
        meas_type = "runtime_error"
        source_dict = next((s for s in self.file_list if s["source"] == source),None)
        meas_dict = next((s for s in source_dict["files"] if s["meas_type"] == "runtime_error"),None)

        if(not meas_dict):
            fh = open(source + "/" + filename + ".txt", "w")
            meas_dict = {"meas_type" : "runtime_error", "file_handle" : fh}
        
        fh = meas_dict["file_handle"]

        if(fh):
            fh.write(str(error))

    
    def close(self):
        for source_dict in self.file_list:
            for meas_dict in source_dict["files"]:
                meas_dict["file_handle"].close()
    
        

