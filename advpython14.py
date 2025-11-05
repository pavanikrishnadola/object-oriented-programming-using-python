#method overridding
class Person:
    def walk(self):
        print("Person wlaks slowly")
class Employee(Person):
    def walk(self):
        print("Employee wlaks speedly")
E=Employee()
E.walk()