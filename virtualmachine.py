from architecture import *

class VirtualMachine:
    def __init__(self):
        self._PC = Register()
        self._register_file = RegisterFile()
        self._memory = Memory()
        self._alu = ALU()
        self._decoder = Decoder() 
        
    def load(self, program_filepath):
        for PC, object_line in enumerate(open(program_filepath, 'r')):
            # hex check
            if len(object_line) < 16:
                object_line = '{0:{fill}{width}b}'.format(int(object_line, 16), fill = '0', width = 16)
            self._memory.write(PC, int(object_line[2:], 2))
    
    def _execute_at_PC(self):
        instruction = self._memory.read(self._PC.read())
        print(instruction)
        
        
        
        pass
        
        
    def step(self):
        
        
        self._execute_at_PC(self)
        
    def run(self):
        pass
    
    def dump_core(self):
        print(self._PC)
        print('\n')
        print(self._register_file)
        print(self._memory)
        
        
        
    