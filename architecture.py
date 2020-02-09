import numpy as np

class Register:
    def __init__(self, gnd = False):
        # init zero
        self._contains = np.int16(0)
        if gnd:
            self._gnd = gnd

    def read(self):
        return self._contains

    def write(self, value):
        if self._gnd:
            return
        else:
            self._contains = np.int16(value)
        
class ProgramCounter(Register):
    def __init__(self):
        Register.__init__(self, gnd = False)
    
    def increment(self):
        self.write(self.read + 1)
        
class RegisterFile:
    def __init__(self):
        r0 = Register(True)
        r1 = Register()
        r2 = Register()
        r3 = Register()
        r4 = Register()
        r5 = Register()
        r6 = Register()
        r7 = Register()
        r8 = Register()
        self._register_file = [r0, r1, r2, r3, r4, r5, r6, r7, r8]
    
    def read(self, register):
        return self._register_file[register].read()
    
    def write(self, register, value):
        self._register_file[register].write(value)

class Memory:
    def __init__(self, size = 1000):
        self.size = size # in shortword addresses
        self._memory = [Register()]*self.size
        
    def read(self, address):
        return self._memory[address].read()
    
    def write(self, address, value):
        self._memory[address].write(value)
        
class ALU:
    def __init__(self):
        pass
    
    
    