#Exception Handling
#program without Exception handling using try...except...finally
a=100;b=2
try:
  print("Begin")
  print("Ready")
  c=a/b
  print("Result=",c)
  print("Division Completed")
  print("End")
except:
  print("You cannot divide number with zero")
else:
  print("Sucess")
finally:
  print("Execution of the code is completed")