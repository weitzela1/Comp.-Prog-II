class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi")

    def __str__(self):
        return ("Animal")

    def __str__(self):
        return "Cat: " + self.name

class Cat(Animal): #inheriting from animal
    # Cat inherits name, age, and say_hi from Animal
    def __init__(self, name, age, sound):
        # Animal.__init__(name, age)
        super().__init__(name, age)
        self.sound = sound

    def say_sound(self):
        print(self.sound)

cat = Cat("Billy", 5 , "Meow")
cat.say_hi()
cat.say_sound()
print(cat)


