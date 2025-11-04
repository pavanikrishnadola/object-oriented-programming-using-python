#constructor
class Calculator:
    def __init__(self):
       self.a=3
       self.b=5
    def putvals(self):
        print("value of a=",self.a)
        print("value of b=",self.b)
    def mysum(self):
        return self.a+self.b
C=Calculator()
C.putvals()
print("Sum=",C.mysum())
del C
