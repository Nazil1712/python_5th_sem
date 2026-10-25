def myFun(*nazil):
    for i in nazil:
        print(i)

myFun("nazil",'mussu','pappu','dhabbu')


def fun2(**dict):
    print("His last name is ", dict['lname'])

fun2(fname="nazil",lname="dhalwala")