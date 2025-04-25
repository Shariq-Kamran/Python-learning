class calculator:

    def __init__(self,num):
        self.num=num
        self.sq=num*num
        self.cube=num**3

    @staticmethod
    def hello():
        print("Hello there...")


number=calculator(12)
print(number.num, number.sq, number.cube)
number.hello()