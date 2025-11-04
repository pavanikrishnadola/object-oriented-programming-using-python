#multilevel inheritance
class A:
    def funca(self):
        print("This is function A")
class B(A):
    def funcb(self):
        print("This is function B")
class C(B):
    def funcc(self):
        print("This is function C")
objB=B()
objB.funca()
objB.funcb()
print("-------------------")
objC=C()
objC.funca()
objC.funcb()
objC.funcc()