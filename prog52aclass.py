class Shape:
    # Constructor:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._area - 0 # ._ basically means 'private' so
        self._perim = 0 # it should only be called in the class

    # Mutator/Setter Method: modifies class data
    def calculate(self):
        self._area = self.length * self.width
        self._perim = 2 * self.length + 2 * self.width

    # Acsessor/Getter Method(s): returns class data
    def get_area(self):
        return self._area
    def get_perim(self):
        return self.perim

    def main():
        length = int(input("Enter Length: "))
        width = int(input("Enter Width: "))
        # Make a new 'Shape' object/instance
        shape = Shape(length, width) # Call 'Shape' constructor/ __init__ method
        # shape.length = 5
        shape.calculate()
        print("Area:", shape.get_area())
        print("Perimeter:", shape.get_perimeter())
        pass

    if __name__ == "__main__":
        main()
