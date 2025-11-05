#multiple inheritance
class A:
    def fofca(self):
        print("Function of class A")
class B:
    def fofcb(self):
        print("Funtion of class B")
class C(A,B):
    def fofcc(self):
        print("Function of class C")
objC=C()
objC.fofca()
objC.fofcb()
objC.fofcc()