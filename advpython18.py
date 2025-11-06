#Exception Handling
#program without Exception handling
a=100;b=0
try:
  print("Begin")
  print("Ready")
  c=a/b
  print("Result=",c)
  print("Division Completed")
  print("End")
except:
  print("You cannot divide number with zero")