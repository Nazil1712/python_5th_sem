# a = (1,2,3)

# print(a)
# print(type(a))
# print(a[0])

# a[0] = 48 #Throws an error because it is Unchangeable
# print(a)


""" b = (1)
c = (1,)
print(type(b))
print(type(c)) """




# Updating tuples
""" myt = tuple((1,2,3,4))
mylist = list(myt)

mylist[0] = 45
myt = tuple(mylist)

print(myt) """


""" b = (4,5,8)
del b
print(b) """


""" t1 = (1,2,3)
t2 = (4,)

t1 += t2
print(t1) """



# Packing - unpacking
""" t1 = tuple(("apple",'banana','cherry')) # => this is known as packing

(green,yellow,red) = t1 # => This is known an Unpacking

print(green)
print(yellow)
print(red) """


t2 = tuple(("apple",'banana','cherry','kiwi','Chiku','guauava'))

# (green,yellow,red,*rem) = t2 
# print(green)
# print(yellow)
# print(red)
# print(rem)


# (red,*rem,green) = t2
# print(red)
# print(rem)
# print(green)




# Joining tuples
a1 = (1,2,3)
a2 = ('a','b','c')

# print(a1+a2)
# print(a1*2)