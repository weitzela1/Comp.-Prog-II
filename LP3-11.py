class percent:
    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1 # designing
        self.n2 = n2 # Coding
        self.n3 = n3 # Debuggging
        self.n4 = n4 # testing
        n1 = int(input("testing"))
        n2 = int(input("testing"))
        n3 = int(input("testing"))
        n4 = int(input("testing"))


    def calc(self):

        self.total = self.n1 + self.n2 + self.n3 + self.n4
        self.n1percent = (self.total / self.n1) * 100
        self.n2percent = (self.total / self.n2) * 100
        self.n3percent = (self.total / self.n2) * 100
        self.n4percent = (self.total / self.n2) * 100

    def getanswer(self):
        return self.n1percent
