def pos(a,b):
    print(a - b)

# pos(5,10)
# pos(10,5)

# pos(a=10,b=5)
# pos(b=5,a=10)

# pos(45,b=5)


def message(name="Guest"):
    print("Hello",name)

# message("Nazil")
# message()


def mysum(*args):
    ans = 0
    for i in args:
        ans += i

    print("sum is : ",ans)

# mysum(1,2,3,4,5)
# mysum(10,20,30,40,50)

def fact(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * fact(n-1)


# print(fact(5))


# Lambda Function
""" x = lambda a : a + 5
print(x(10)) """

def myFunc(n):
    return lambda a : a * n

doubler = myFunc(2)

print(doubler(5))