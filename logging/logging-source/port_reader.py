import serial
import collections
import threading

class PortReader(threading.Thread):
    def __init__(self,port = 6230, baud_rate = 9600, max_size = 256):
        self.ser = serial.Serial(port = port, baudrate = baud_rate)
        self.errors = []
        self.packet_queue = collections.deque()
        threading.Thread.__init__(self)

    def next_packet(self):
        if(len(self.packet_queue)>0):
            return self.packet_queue.popleft()        
        return None

    def run(self):
        if(not self.ser.is_open):
            self.ser.open()
        try:
            while(self.ser.is_open):    
                data = self.ser.readline().rstrip()

                # NEED A CHECKSUM HERE

                self.packet_queue.append(data)#[:-1]
        except serial.SerialException as err:
            self.errors.append(err)
            print("Error reading from serial port ",self.ser.port)
            self.ser.close()
            
    
    def get_errors(self):
        return self.errors


    