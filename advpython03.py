#Basic Calculator
class Calculator:
    def getvals(self):
        self.a=int(input("Enter value of a:"))
        self.b=int(input("Enter value of b:"))
    def putvals(self):
        print("value of a=",self.a)
        print("value of b=",self.b)
    def mysum(self):
        return self.a+self.b
    def mysub(self):
        return self.a-self.b
    def mymul(self):
        return self.a*self.b
    def mydiv(self):
        return self.a/self.b
    def myfdiv(self):
        return self.a//self.b
    def mymod(self):
        return self.a%self.b
    def myexp(self):
        return self.a**self.b
Casio=Calculator()
Casio.getvals()
Casio.putvals()
print("-------------------------------")
print("MENU")
print("-------------------------------")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.FLOOR DIVISION")
print("6.MODULUS")
print("7.EXPONENTATION")
print("--------------------------------")
x=int(input("Select one option from the above:"))
print("--------------------------------")
if(x==1):
    print("ADDTION=",Casio.mysum())
elif(x==2):
    print("SUBTRACTION=",Casio.mysub())
elif(x==3):
    print("MULTIPLICATION=",Casio.mymul())
elif(x==4):
    print("DIVISION=",Casio.mydiv())
elif(x==5):
    print("FLOOR DIVISION=",Casio.myfdiv())
elif(x==6):
    print("MODULUS=",Casio.mymod())
elif(x==7):
    print("EXPOTENTATION=",Casio.myexp())
else:
    print("Invalid Option")