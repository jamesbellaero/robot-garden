class CrcChecksum:
    def __init__(self, aPattern = 0x4C036099):
        self.pattern = aPattern & pow(256,4)
        self.crcTable = [0]*256
        self.initalized = False
    def initialize_crc_table(self):
        eight_bits = pow(2,8)
        thirty_two_bits = pow(eight_bits,4)
        self.crcTable[0] = 0

        # Check this for error
        crc = 1

        i = 128
        while(i>0):
            if(crc & 1):
                crc = ((crc >> 1)^self.pattern) 
            else:
                crc = (crc >> 1) 
            # Ensure typing as uint32_t
            crc &= thirty_two_bits

            for j in range(0,256,2*i):
                self.crcTable[i+j] = (crc^self.crcTable[j]) & eight_bits
            
            i = i>>1

    def set_pattern(self, aPattern):
        self.pattern = aPattern
    def get_patter(self):
        return self.pattern
    def calculate_crc(self, data):
        # Data can be a string, list of characters, or list of ints

        eight_bits = pow(2,8)
        remainder  = 0
        if(isinstance(data[0],str)):
            data = list(data) # If it's a list of strings already, this call does nothing of import
            for i in range(0,len(data)):
                data[i] = ord(data[i])

        for i in range(0,len(data)):
            remainder = remainder ^ data[i]

            rightmost = remainder & eight_bits
            remainder = (remainder>>8)^self.crcTable[data[i] ^ rightmost]

        crc = [0]*4
        for i in range(0,4):
            crc[i] = (remainder >> (i-1)*8) & eight_bits

        
        return crc
