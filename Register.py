"""This class represents a Register in a Device that can be written and read.
"""

class Register(object):
    
    def __init__(self, data, size, can_write):
        self.data = data            # Hexadecimal value for register contents
        self.size = size            # Size in bits of the register
        self.can_write = can_write  # boolean for whether register can be written to


    def write(self, new_data):
        """If the register is writeable, write new data."""
        if self.can_write:
            self.data = new_data
        else:
            raise IOError("Attempted write to readonly register")
            
        
    def __str__(self):
        """Returns a string representation of this Register."""
        return f'Contents: {hex(self.data)}\nSize: {self.size} bits\n{"Read/Write" if self.can_write else "Read-only"}\n'


# Debugging code
if __name__ == "__main__":
    r0 = Register(0xFF, 8, False)
    r1 = Register(0x01, 8, False)
    r2 = Register(0x03, 8, False)
    r3 = Register(0x11, 8, False)
    print(r0.data)
    print(str(r2))