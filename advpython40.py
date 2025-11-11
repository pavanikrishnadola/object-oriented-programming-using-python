class Icecream:
    def melts(self):
        print("It melts at room temp")
    def billamt(self):
        return self.price*self.quantity
Vanilla=Icecream()
Vanilla.price=20
Vanilla.quantity=500
Vanilla.wt=45.5
Vanilla.color="vanilla white"
print("Price of vanilla=",Vanilla.price)
print("Qantity of vanilla=",Vanilla.quantity)
print("Wt of vanilla=",Vanilla.wt)
print("Color of vanilla=",Vanilla.color)
Vanilla.melts()