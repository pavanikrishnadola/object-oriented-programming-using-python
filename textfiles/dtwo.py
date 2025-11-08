import pickle
f=open("emp.dat","rb")
x=pickle.load(f)
print(x)