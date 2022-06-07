from MenuItem import MenuItem

class Cake(MenuItem):
    def __init__(self, name, price, flavour):
        super().__init__(name, price)
        self.flavour = flavour
    
    def info(self):
        return self.name + '\t : RP.' + str(self.price) + ' (' + str(self.flavour) + ')'
