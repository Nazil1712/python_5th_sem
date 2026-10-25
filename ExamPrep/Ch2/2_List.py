""" myList = ["apple","banana","orange"]

print(myList)
print(myList[0]) #indexed

myList[0] = "mango" #changeable
print(myList)

print(len(myList)) """


""" a = list((1,2,3,4))
print(type(a)) """



# Accessing List
a = ["apple","banana","mango","orange",'melon','kiwi','guava','custardApple']

""" print(a[-1])
print(a[0:-1])
print(a[-4:-1]) """


# Changing list items
""" a[0:3] = ['nazil','mussu','tomato']
print(a) """

""" a[0:3] = ['bomb']
print(a) """



# List methods
b = [1,2,3]


# Adding
""" print(len(b))
b.insert(0,15)
b.append(48)

c = [10,11,12]
b.extend(c)
print(b) """


# removing
""" b.remove(3)
b.pop(0)

del b[1]
del b
print(b) """



# Looping
d = ['paneer','potato','tomato']

""" for i in d:
    print(i) """


""" for i in range(len(d)):
    print(d[i]) """


""" i = 0
while i < len(d):
    print(d[i])
    i = i + 1 """


""" [print(i,end=" ") for i in d] """


# sorting
""" num = [5,4,3,2,1]
num2 = [1,2,3,4,5]

num.sort()
num2.sort(reverse=True)

print(num)
print(num2) """


a1 = [1,2,3,4,4,4]
# a1.clear()
# print(a1)

# print(a1.count(4))

# a2 = a1.copy()
# print(a1 is a2)



l1 = [1,2,3,4]
# l2 = l1
# l2 = list(l1)
# l2 = l1[:]

print(l1 is l2)