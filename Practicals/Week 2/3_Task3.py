principal = float(input("Enter the principal amount: "))
years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))

# Convert interest rate to decimal
interest_rate_decimal = interest_rate / 100

# Calculate compound interest
compound_interest = principal * (1 + interest_rate_decimal) ** years - principal

print("Compound Interest:", compound_interest)
