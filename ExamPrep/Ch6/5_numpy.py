import numpy as np

""" a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
print(a+b) """

""" 
a = np.zeros((2,4))
b = np.ones((2,4))
c = np.empty((2,4))
d = np.arange(5)
e = np.identity((5))

# print(a)
# print(d)
print(e) """


a = np.random.randint(100)
# print(a)

b = np.random.rand()
# print(b)

c = np.random.randint(100,size=(3,5))
# print(c)

d = np.random.rand(3,5)
# print(d)


# Vstack
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([5,6])
# print(np.vstack((arr1,arr2)))


# hstack
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6],[7,8]])
print(np.hstack((arr3,arr4))) 

""" a = np.array([1,2,3,4])
b = np.array([1,2,2,4]) 
np2d = np.array([[1.73,1.68,1.71,1.89,1.79],
                 [65.4,59.2,63.6,88.4,68.7]]) """


# print(np2d.shape)
# print(np2d[0])
# print(np2d[1])
# print(np2d[:,1:3])
# print(np2d[1,:])
# print(np.mean(np2d))
# print(np.std(np2d))
# print(np.median(np2d))
# print(np2d > 5)
# print(np2d[np2d>5])

# s1 = "Hi my name is Nazil"
# print(s1[5:0:-1])