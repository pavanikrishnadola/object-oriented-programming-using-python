#hierarichal
class A:
    def funca(self):
        print("This is function A")
class B(A):
    def funcb(self):
        print("This is function B")
class C(A):
    def funcc(self):
        print("This is function C")
class D(A):
    def funcd(self):
        print("This is function D")
objB=B()
objB.funca()
objB.funcb()
print("-------------------")
objC=C()
objC.funca()
objC.funcc()
print("-------------------")
objD=D()
objD.funca()
objD.funcd()
print("-------------------")