for num in range(1, 101):
    if num % 4 == 0 and num % 6 == 0:
        print("CHARUSAT_IT")
    elif num % 4 == 0:
        print("IT")
    elif num % 6 == 0:
        print("CHARUSAT")
    else:
        print(num)
