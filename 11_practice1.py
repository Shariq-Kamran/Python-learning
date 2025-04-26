class TwoD_vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

class TreeD_vector(TwoD_vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k

a=TwoD_vector(1,2)
b=TreeD_vector(1,4,3)
print(a.i,a.j)
print(b.i,b.j,b.k)