class Instruction:
    _RRR = {'000': 'add', '010': 'nand'}
    _RRI = {'001': 'addi', '101': 'sw', '100': 'lw', '110': 'beq', '111': 'jalr'}
    
    def __init__(self, instruction_string):
        self._instruction_string = instruction_string
        self.opcode = self._get_opcode
        if self.opcode in self._RRR:
            
    def _get_opcode(self):
        return self._instruction_string[:3]
    
    def 