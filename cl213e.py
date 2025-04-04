import random
class FamStats:
    numcount = random.randint(10, 30)
    def __init__(self, age, g1, g2, g3, g4, g5, total):
        self.age = random.randint(1,100)
        self.g1 = 0
        self.g2 = 0
        self.g3 = 0
        self.g4 = 0
        self.g5 = 0
        self.total = 0
    def calc(self, g1, g2, g3, g4, g5, total):
        if self.age < 20:
            g1 +=1
        elif self.age >= 20 and self.age < 40:
            g2 +=1
        elif self.age >= 40 and self.age < 60:
            g3 += 1
        elif self.age >= 60 and self.age < 80:
            g4 += 1
        elif self.age > 80:
            g5 += 1
        else:
            pass
        self.total = g1 + g2 + g3 + g4 + g5











