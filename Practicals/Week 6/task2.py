def get_salary_details(basic_salary):
    DA = basic_salary * 0.7
    MA = 100
    TA = 400
    TOTAL_SALARY = basic_salary + DA + MA + TA

    print(f"DA: {DA}")
    print(f"MA: {MA}")
    print(f"TA: {TA}")
    print(f"TOTAL_SALARY: {TOTAL_SALARY}")

    return DA, MA, TA, TOTAL_SALARY


basic_salary = float(input("Enter basic salary: "))
da, ma, ta, total_salary = get_salary_details(basic_salary)
