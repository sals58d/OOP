from MenuItem import MenuItem

class Ice(MenuItem):
    def __init__(self, name, price, toping):
        super().__init__(name,price)
        self.toping = toping
    
    def info(self):
        return self.name + '\t: RP.' + str(self.price) + ' (' + str(self.toping) + ')'
