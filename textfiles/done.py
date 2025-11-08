import pickle
emp_det=[101,"raj",4566.75,"a"]
f=open("emp.dat","wb")
pickle.dump(emp_det,f)
f.close()