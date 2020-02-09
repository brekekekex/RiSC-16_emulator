from disassembler import *

class Emulator:
    def __init__(self, program_filepath, verbose_disassembler = True):
        self.program_filepath = program_filepath
        self.verbose_disassembler = verbose_disassembler
        
    def emulate(self):
        myDisassembly = Disassembler(self.program_filepath)
        disassembled_file = myDisassembly.Disassemble()
        print(disassembled_file)
        
        
    
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--novd', required = False, action = 'store_false', help = 'verbose disassembler--show disassembled file')
    argument = parser.parse_args()

    myEmulator = Emulator(argument.filename, argument.novd) 
    myEmulator.emulate()