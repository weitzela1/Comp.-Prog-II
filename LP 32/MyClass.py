class pizza:
    def __init__(self, diam):
        self.diam = diam
        self.total = 0
        
    def calc(self):
        self.total = (self.diam * self.diam * 0.05) + 1.75
        
    def get_calc(self):
        print(round(self.total, 2))
        
     
        