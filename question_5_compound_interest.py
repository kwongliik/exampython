def compound_interest(principal, rate, time, n):
    result = principal * (pow(1 + rate / (100*n), n*time))
    return result

def calculate_and_print_interest():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the interest rate: "))
    t = float(input("Enter the time in years: "))
    n = float(input("Enter the number of periods the interest is compounded per year: "))

    interest = compound_interest(p, r, t, n)
    print("Compound interest is %.2f" % interest)

if __name__ == "__main__":
    calculate_and_print_interest()