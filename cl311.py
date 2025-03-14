class Application:
    def __init__(self, des, cod, debug, test):
        self.des = des
        self.cod = cod
        self.debug = debug
        self.test = test
        self.total = 0
    def calctotal(self):
        self.total = self.des + self.cod + self.debug + self.test

    def calcpercent(self):
        self.des = (self.des/self.total) * 100
        self.cod = (self.cod/self.total) * 100
        self.debug = (self.debug/self.total) * 100
        self.test = (self.test/self.total) * 100

    def show(self):
        print(round(self.des, 2))
        print(round(self.cod, 2))
        print(round(self.debug, 2))
        print(round(self.test, 2))






