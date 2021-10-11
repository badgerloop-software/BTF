# This class represents a Register in a Device that can be written and read.

class Register:
    def __init__(self, data, size):
        self.data = data
        self.size = size

#Testing to see if it works?
    def print_info(self):
        print(self.data, ',', self.size)

r = Register('0000000', '8')
r.print_info()