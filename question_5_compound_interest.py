# This program is used to calculate compound interest.
# User can input 
# (a) principal, 
# (b) interest rate, 
# (c) time in years, and 
# (d) number of periods the interest is compounded per year (n)
# You need to complete the code below.
# Upon completion, you should test run the code to give you correct output.

# compound_interest() is a function that will return the result of calculation
def compound_interest(principal, rate, time, n):
    result = principal * (.....(1 + ..... / (.......), ........)) # Use built-in function "pow()" to complete the formula
    return result 

def calculate_and_print_interest():
    p = float(input("Enter the principal amount: ")) # Don't change the code
    r = float(input("Enter the interest rate: ")) # Don't change the code
    t = float(input("Enter the time in years: ")) # Don't change the code
    n = float(input("Enter the number of periods the interest is compounded per year: ")) # Don't change the code

    interest = ...............(p, r, t, n) # Call the function to calculate compound interest
    print("Compound interest is %.2f" % interest) # Don't change the code

# Don't change the code below!
if __name__ == "__main__":
    calculate_and_print_interest()
