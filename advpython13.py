#multipath inheritance
class A:
    def fofca(self):
        print("Function of class A")
class B(A):
    def fofcb(self):
        print("Function of class B")
class D(A):
    def fofcd(self):
        print("Function of class D")
class C(B,D,A):
    def fofcc(self):
        print("Function of class C")
objC=C()
objC.fofca()
objC.fofcb()
objC.fofcc()
objC.fofcd()