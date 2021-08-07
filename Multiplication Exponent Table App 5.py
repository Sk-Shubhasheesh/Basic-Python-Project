# Hello, In the 5th challenge we create a Multiplication Exponent Table App
print("Welcome to the Multiplication/Exponent Table Program")
name = input("\nHello, What is your Name: ").title().strip()
print("Hello, " + name + "!")
num = float(input("What number would you like work with: "))
message = name + ", Math is Cool!"
# multiplication table:

print("\nMultiplication Table For " , str(num))
print("1.0 * " + str(num) + " = " ,str(round(1*num, 4)))
print("2.0 * " + str(num) + " = " +str(round(2*num, 4)))
print("3.0 * " + str(num) + " = " +str(round(3*num, 4)))
print("4.0 * " + str(num) + " = " +str(round(4*num, 4)))
print("5.0 * " + str(num) + " = " +str(round(5*num, 4)))
print("6.0 * " + str(num) + " = " +str(round(6*num, 4)))
print("7.0 * " + str(num) + " = " +str(round(7*num, 4)))
print("8.0 * " + str(num) + " = " +str(round(8*num, 4)))
print("9.0 * " + str(num) + " = " +str(round(9*num, 4)))
print("10.0 * " + str(num) + " = " +str(round(10*num, 4)))
# Exponent Table:

print("\nExponent Table For " + str(num))
print("\n" +str(num) + " **1 = " +str(round(num**1, 4)))
print(""+str(num) + " **2 = " +str(round(num**2, 4)))
print(""+str(num) + " **3 = " +str(round(num**3, 4))) 
print(""+str(num) + " **4 = " +str(round(num**4, 4)))
print(""+str(num) + " **5 = " +str(round(num**5, 4)))
print(""+str(num) + " **6 = " +str(round(num**6, 4)))
print(""+str(num) + " **7 = " +str(round(num**7, 4)))
print(""+str(num) + " **8 = " +str(round(num**2, 4)))
print(""+str(num) + " **9 = " +str(round(num**9, 4)))
print(""+str(num) + " **10 = " +str(round(num**10, 4)))

# MAth is cool:
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())
