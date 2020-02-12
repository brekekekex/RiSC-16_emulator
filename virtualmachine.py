from architecture import *

class VirtualMachine:
    def __init__(self):
        self._alu = ALU()
        self._register_file = RegisterFile() 
        self._register_file.write(1, 3)
        self._register_file.write(2, 5)
        print(self._register_file)
        self._alu.do_nand(self._register_file[3], self._register_file[2], self._register_file[1])
        print(self._register_file)
        
        
        
        
    def dump_core(self):
        pass
        
        
        
    