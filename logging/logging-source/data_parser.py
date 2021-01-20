import json
import logging_types

class DataParser:
    def __init__(self):
        self.errors = []
        # There should be a dictionary here to map json to measurement variables
        # Or maybe that should be elsewhere. Whatever.

    def parse_packet(self,packet):
        json_data = None
        try:
            json_data = json.loads(packet)
        except json.JSONDecodeError as json_err:
            self.errors.append(json_err)
            print("Error deserializing JSON data")
        if(json_data is None):
            return
        
        source = json_data.source
        meas_type = json_data.meas_type
        time = json_data.time
        value = json_data.value

        measurement = logging_types.Measurement(source,meas_type,time,value)

        return measurement

    def get_errors(self):
        return self.errors
