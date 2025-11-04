#Inheritance
#single Inheritance
class A:
    def funca(self):
        print("This is function A")
class B(A):
    def funcb(self):
        print("This is function B")
objB=B()
objB.funca()
objB.funcb()