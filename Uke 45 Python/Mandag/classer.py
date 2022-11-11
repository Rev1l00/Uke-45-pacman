class pizza():
    def __init__(self, mel, gjær, vann, salt):
        self.mel = mel
        self.gjær = gjær
        self.vann = vann
        self.salt = salt

    def ovn(self):
        self.temperature = 200
        self.time = 20
        self.bunn_pizza = self.mel + self.gjær + self.vann + self.salt + self.temperature + self.time
        return self.bunn_pizza
    
pizza_box = pizza(0.5, 1, 0.4, 0.02)
print(pizza_box.ovn())