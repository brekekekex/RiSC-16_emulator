class Register:
    def __init__(self, gnd = False):
        self._gnd = gnd
        self._signed = False 
        self._content = (0).to_bytes(2, byteorder = 'big', signed = self._signed)
        
    def read(self):
        return int.from_bytes(self._content, byteorder = 'big', signed = self._signed)
    
    #def read_literal(self):
    #    return self._content
        
    def write(self, value):
        self._signed = (value < 0)
        if not self._gnd:
            self._content = (value).to_bytes(2, byteorder = 'big', signed = self._signed)
            
    def increment(self):
        self.write(self.read() + 1)
                 
    def __str__(self):
        return '[0d]\t' + str(self.read())      
        
class RegisterFile:
    def __init__(self):
        self._content = [Register(gnd = True)]
        for i in range(7):
            register = Register()
            self._content.append(register)
            
    def read(self, register):
        return self._content[register].read()
        
    def write(self, register, value):
        self._content[register].write(value)
        
    def __str__(self):
        return_string = ''
        for register in self._content:
            return_string = return_string + str(register) + '\n'
        return return_string
    
    def __getitem__(self, key):
        return self._content[key]
        
class Memory:
    _DEFAULT_NUM_WORDS = 20
    
    def __init__(self):
        self._content = []
        for i in range(self._DEFAULT_NUM_WORDS):
            address = Register()
            self._content.append(address)
            
    def read(self, address):
        return self._content[address].read()
    
    def write(self, address, value):
        self._content[address].write(value)
    
    def __str__(self):
        return_string = ''
        for address in self._content:
            return_string = return_string + str(address) + '\n'
        return return_string
    
class ALU:
    def __init__(self):
        self._special = Register()
    
    def do_add(self, register_A, register_B, register_C):
        register_A.write(register_B.read() + register_C.read())
        
    def do_addi(self, register_A, register_B, immed):
        self._special.write(immed)
        register_A.write(register_B.read() + self._special.read())
    
    def do_nand(self, register_A, register_B, register_C):
        register_A.write(~(register_B.read() & register_C.read()))
    
class Decoder:
    def __init__(self):
        pass
    
    def decode(self, instruction):
        
        
        
        
        pass
        
        