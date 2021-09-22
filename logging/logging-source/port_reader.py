import serial
import collections
import threading

class PortReader(threading.Thread):
    def __init__(self,port = 6230, baud_rate = 9600, max_size = 256):
        self.ser = serial.Serial(port = port, baudrate = baud_rate)
        self.errors = []
        self.packet_queue = collections.deque()
        self.checksum_pattern = bin(0x4C036099)[2:]
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
                print(data)
                # CHECKSUM HERE
                # convert everything to bits
                data_bits = []
                crc_length = 0
                for i in range(len(data)):
                    eight_zeros = '00000000'
                    bits = bin(data[i])[2:]
                    data_bits.append(eight_zeros[len(bits):]+bits)
                i = len(data_bits)
                # Take the pattern and xor consecutively along the value at each 1
                while i > len(data_bits) - len(self.checksum_pattern):
                    data_bits = self.xor_lists(data_bits[i:],self.checksum_pattern)
                    i_new = data_bits.find('1')
                    if(i_new == i):
                        self.errors.append(Exception("Cyclic Redundancy Check failed"))
                 #       print(data_bits)
                 #       print("failed\n")

                        break
                #print(data_bits)
                #print("success\n")

                if( i > 0):
                    return
                # If it's not, log the error and return
                # If it's zero, remove the last 32 bits and append the data
                packet = data[0:data.find(b'}')+1]
                self.packet_queue.append(packet)#[:-1]
        except serial.SerialException as err:
            self.errors.append(err)
            print("Error reading from serial port ",self.ser.port)
            self.ser.close()
            
    def xor_lists(self,list1,list2):
        n = min(len(list1),len(list2))
        result = [0]*n
        for i in range(n):
            result[i] = list1[i] ^ list2[i]
        if(len(list1) > len(list2)):
            result.append(list1[n:])
        elif(len(list1) < len(list2)):
            result.append(list2[n:])
        return result

    def get_errors(self):
        return self.errors


    