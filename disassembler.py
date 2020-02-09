class Disassembler:
    def __init__(self, program_filepath):
        self.program_filepath = program_filepath
    
    def Disassemble(self):
        self.disassembled_file = DisassembledFile()
        for PC, object_line in enumerate(open(self.program_filepath, 'r')):
            # hex check
            if len(object_line) < 16:
                object_line = '{0:{fill}{width}b}'.format(int(object_line, 16), fill = '0', width = 16)
            self.disassembled_file.add(Instruction(object_line.strip(), PC))
        return self.disassembled_file
    
class DisassembledFile:
    def __init__(self):
        self._contains = []
    
    def add(self, instruction):
        self._contains.append(instruction)
    
    def __repr__(self):
        output_string = '\n[PC]\t[Machine]\t[Instruction]\n'
        for instruction in self._contains:
            output_string = output_string + '0x{0:0{1}X}'.format(instruction.get_PC(),4)[2:] + '\t' + instruction.get_hex_string() + '\t' + str(instruction) + '\n'
        return output_string
        
class Instruction:
    _RRR = {'000': 'add', '010': 'nand'}
    _RRI = {'001': 'addi', '100': 'sw', '101': 'lw', '110': 'beq', '111': 'jalr'}
    _RI = {'011': 'lui'}
    _registers = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7} 
    
    def __init__(self, instruction_string, PC):
        self._instruction_string = instruction_string
        self._hex_string = '0x{0:0{1}X}'.format(int(self._instruction_string, 2),4)[2:]
        self._PC = PC
        self.opcode = self._get_opcode()
        if self.opcode in self._RRR:
            self.type = 'RRR'
            self._register_A = self._registers[self._get_reg('A')]
            self._register_B = self._registers[self._get_reg('B')]
            self._register_C = self._registers[self._get_reg('C')]
        elif self.opcode in self._RRI:
            self.type = 'RRI'
            self._register_A = self._registers[self._get_reg('A')]
            self._register_B = self._registers[self._get_reg('B')]
            self._signed_imm = int(self._get_signed_imm(), 2)
        elif self.opcode in self._RI:
            self.type = 'RI'
            self._register_A = self._registers[self._get_reg('A')]
            self._unsigned_imm = int(self._get_unsigned_imm(), 2)
            
    def _get_opcode(self):
        return self._instruction_string[:3]
    
    def _get_reg(self, register):
        if register == 'A':
            return self._instruction_string[3:6]
        elif register == 'B':
            return self._instruction_string[6:9]
        elif register == 'C':
            return self._instruction_string[-3:]
    
    def _get_signed_imm(self):
        return self._instruction_string[-7:]
    
    def _get_unsigned_imm(self):
        return self._instruction_string[-10:]
    
    def __str__(self):
        if self.type == 'RRR':
            return '\t' + self._RRR[self.opcode] + '\t' + 'r' + str(self._register_A) + ', ' + 'r' + str(self._register_B) + ', ' + 'r' + str(self._register_C)
        elif self.type == 'RRI':
            return '\t' + self._RRI[self.opcode] + '\t' + 'r' + str(self._register_A) + ', ' + 'r' + str(self._register_B) + ', ' + str(self._signed_imm)
        elif self.type == 'RI':
            return '\t' + self._RI[self.opcode] + '\t' + 'r' + str(self._register_A) + ', ' + str(self._unsigned_imm)
        
    def get_PC(self):
        return self._PC
    
    def get_hex_string(self):
        return self._hex_string