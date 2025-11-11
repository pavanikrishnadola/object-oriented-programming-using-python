class Calculator:
    def Putvalues(self):
        print("value of a=",self.a)
        print("value of b=",self.b)
    def add(self):
        return self.a+self.b
Casio=Calculator()
Casio.a=5
Casio.b=3
Casio.Putvalues()
print("Sum=",Casio.add())