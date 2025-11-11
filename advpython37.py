class Bird:
    def fly(self):
        print("They fly to fulfill their natural activities")
    def buildnest(self):
        print("They bilud nest to live")
Parrot=Bird()
Parrot.age=4
Parrot.wings=2
Parrot.wt=4.5
Parrot.color="green"
print("Age of parrot=",Parrot.age)
print("Wings of parrot=",Parrot.wings)
print("Wt of parrot=",Parrot.wt)
print("Color of parrot=",Parrot.color)
Parrot.fly()
Parrot.buildnest()
print("-----------------------------------------------------------")
Pigeon=Bird()
Pigeon.age=4
Pigeon.wings=2
Pigeon.wt=5
Pigeon.color="lightgrey"
print("Age of pigeon=",Pigeon.age)
print("Wings of pigeon=",Pigeon.wings)
print("Wt of pigeon=",Pigeon.wt)
print("Color of pigeon=",Pigeon.color)
Pigeon.fly()
Pigeon.buildnest()