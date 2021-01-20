import serial
import collections
import threading

class PortReader(threading.Thread):
    def __init__(self,port = 6230, baud_rate = 9600, max_size = 256):
        self.s = serial.Serial(port = port, baudrate = baud_rate)
        self.errors = []
        self.packet_queue = collections.deque()
        threading.Thread.__init__(self)

    def next_packet(self):
        if(len(self.packet_queue)>0):
            return self.packet_queue.popleft()        
        return None

    def run(self):
        try:
            self.s.open()
            while(self.s.is_open()):    
                data = self.s.readline()
                self.packet_queue.append(data)
        except serial.SerialException as err:
            self.errors.append(err)
            print("Error reading from serial port ",self.s.port)
    
    def get_errors(self):
        return self.errors


    