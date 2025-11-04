#Area of rectangle
class Rectangle:
    def getvals(self):
        self.l=int(input("Enter Length:"))
        self.b=int(input("Enter Breadth:"))
    def putvals(self):
        print("Length=",self.l)
        print("Breadth=",self.b)
    def carea(self):
        return self.l*self.b
R=Rectangle()
R.getvals()
R.putvals()
print("Area Of Rectangle=",R.carea())