import json

class DataParser:
    def __init__(self):

    

    def parse_packet(self,packet):
        try:
            json_data = json.loads(packet)
        except json.JSONDecodeError as json_err:
            self.errors.append(json_err)
            print("Error deserializing JSON data")







