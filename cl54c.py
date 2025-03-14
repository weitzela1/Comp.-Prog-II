class Application:
     def __init__(self, rad):
          self.rad = rad
          self.pi = 3.14159
          self.circum = 0
          self.area = 0

     def calc(self):
          self.circum = self.rad * 2 * self.pi
          self.area = (self.rad ** 2) * self.pi

     def show(self):
          print(round(self.circum, 2))
          print(round(self.area, 2))
