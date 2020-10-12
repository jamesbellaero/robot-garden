

class Measurement:
    def init(self, source = "Undefined source", meas_type = "Undefined measurement", time = -1, value = 0):
        self.source = source
        self.meas_type = meas_type
        self.time = time
        self.value = value