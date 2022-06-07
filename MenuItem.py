class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': Rp.' + str(self.price)

    def total_price(self, count):
        total_price = self.price * count

        if count >= 3:
            total_price *= 0.9

        return round(total_price)
