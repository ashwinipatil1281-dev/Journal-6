P = float(input("Enter the principal amount (P): "))
R = float(input("Enter the annual interest rate (R) in %: "))
T = float(input("Enter the time period (T) in years: "))

# Calculate simple interest
SI = (P * R * T) / 100

# Display the result
print(f"\nSimple Interest = {SI:.2f}")