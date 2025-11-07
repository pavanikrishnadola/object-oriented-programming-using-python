#user define exception
class InvalidAgeException(Exception):
    pass
age=int(input("Enter Your Age:"))
try:
    if(age<18):
        raise InvalidAgeException
except:
    print("Not ok")
else:
    print("Ok")
finally:
    print("Ask others to vote")