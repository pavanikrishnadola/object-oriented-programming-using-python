#hybrid inheritance
class A:
    def fofca(self):
        print("Function of class A")
class B(A):
    def fofcb(self):
        print("Funtion of classs B")
class C:
    def fofcc(self):
        print("Function of class C")
class D(B,C):
    def fofcd(self):
        print("Function of class D")
objD=D()
objD.fofca()
objD.fofcb()
objD.fofcc()
objD.fofcd()