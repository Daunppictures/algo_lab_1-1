class SignalGenerator(object):
    
    def __init__(self, max_signal_frequency_in_megahz: int, memory_capacity_in_kb: int, brand: str):
        self.max_signal_frequency_in_megahz = max_signal_frequency_in_megahz
        self.memory_capacity_in_kb = memory_capacity_in_kb
        self.brand = brand
