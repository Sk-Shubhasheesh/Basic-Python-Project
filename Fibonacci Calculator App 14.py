# Hello, In the 14th challenge we create a Fibonacci Calculator  App Program
print("Welcome to the Fibonacci Calculator  App")

# Get user input
num = int(input("\nHow many digits of the Fibonacci Sequence would like to compute:"))

# Compute the value of fib
fib = [1,1]
for i in range(num-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)


# Display the fib value
print("\nThe first " + str(num) + " numbers os the Fibonacci Sequence are :")
for number in fib:
    print(number)
# Compute the golden ratio
golden = []
for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)

# Display he golden ratio values
print("\nThe corresponding Golden Ratio values are :")
for ratios in golden:
    print(ratios)
print("\nThe Ratio of the consecutive Fibonacci terms approaches Phi; 1.618...")



