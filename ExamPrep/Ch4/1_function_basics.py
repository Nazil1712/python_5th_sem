# from random import randint
import random

def myFun(name, time):
    """ Hi this is nazil over here
        How are you ? 
        Are you ok?
        What are you doing now a days
    """
    print("Hey ",name," welcome to meem ltd.")
    print("Your death is ",time)

# myFun("nazil","soon")
# print(random.randint(1,5))
# print(myFun.__doc__)
# help(myFun)



""" def isEven(*tup):
    mylist = []
    for i in tup:
        if i%2 == 0:
            mylist.append(i)
    return mylist


even = isEven(1,2,3,4,5,6)
print(even) """



""" def oper(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    return add, sub, mul, div

a = oper(5,2)
print(a)
 """



""" def gl():
    global a
    a = 5
    print(a)

def f2():
    print(a)

gl()
f2()
print("Printing from gloabal ", a) """



def f1():
    x = 78
    print("x in f1 before ", x)

    def f2():
        nonlocal x
        x = 40
        print("x in f2 : ",x)
    
    f2()
    print("x in f1 after ", x)

f1()