class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def Bark():
        print("whof whof")

dog=Dog()
dog.Bark()