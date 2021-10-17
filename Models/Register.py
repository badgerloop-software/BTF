# This class represents a Register in a Device that can be written and read.
# Instance fields:
#   data: hexadecimal value representing register contents
#   size: size of the register in bits

class Register:
    ''' 
    Instance constructor
    '''
    def __init__(self, data, size, can_write):
        self.data = data
        self.size = size
        self.can_write = can_write

    # If the register is writeable, write new data.
    def write(new_data):
        if can_write:
            self.data = new_data
        

#Testing to see if it works?
    def print_info(self):
        print(self.data, ',', self.size, self.can_write)

# Test code
if __name__ == "__main__":
    r0 = Register(0xFF, 8, False)
    r1 = Register(0x01, 8, False)
    r2 = Register(0x03, 8, False)
    r3 = Register(0x11, 8, False)
    print(r0.data)
    r2.print_info()