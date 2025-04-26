class myComplex:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return myComplex(self.a + other.a, self.b + other.b)
    
    
    def __mul__(self, other):
        return myComplex((self.a * other.a - self.b * other.b),(self.a*other.b + self.b*other.a) )

    def __str__(self):
        return f"{self.a} + {self.b}i"

num1=myComplex(1,1)
num2=myComplex(3,5)
print(num1 + num2)
print(num1 * num2)