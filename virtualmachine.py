from architecture import *

class VirtualMachine:
    def __init__(self, program_filepath):
        self._register_file = RegisterFile()
        self._memory = Memory()
        self._PC = ProgramCounter()
        self._program_filepath = program_filepath
        self._program_file = []
        
    def dump_core(self):
        
        
        
    