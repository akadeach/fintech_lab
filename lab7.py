import numpy as np

#1
dat = np.array([1,2,3,4,5,6,7,8,9,10])

print(dat)

#2
print("Shape of dat : ",dat.shape)


#3
print("2nd element in dat : ",dat[1])

#4
print("last 5 elements in dat : ",dat[5:])

#5
dat = np.insert(dat,[1],[50])
print("Assign 50 to the second element in dat : ",dat)

#6
print("Sum of all elements in dat : ",np.sum(dat))
