# #literals
# #Explain the difference b\w "=" operator and "=="operator in python

a = 10
b = 12   # Here we are using "=" is an assignment operator
print(a < b)
print(a > b)
print("\t")

# now I will try with "==" operator which is generally called as Compare operator

Number_1 = (int(input("enter Number_1")))
Number_2 = (int(input("enter Number_2")))
print(Number_1)
print(Number_2)
Compare = Number_1 == Number_2
print("Comparision of Two numbers is",Compare)
print("\t")

# #  "**" operator refers to POWER of assigned value and the same way "*" is multiply

Q = int(input("Enter the number you want to check the power value"))
print(Q)
Power = Q ** Q
print("Power value of the given number is ", Power)
print("\t")

# "^" Bitwise XOR operator

K = int(input("Enter the value of K"))
Q = int(input("Enter the value of Q"))
print(K)
Power = K ^ Q
print("value of the K^Q is ", Power)
print("\t")

# Task-05
# Write a program that takes two numbers as input and prints whether the first number is greater
# than or less than or equal to second number

A = int(input("enter the value of A"))
B = int(input("enter the value of B"))
print("The compare of A and B is ", A == B)
print("A is less than B =", A <= B)
print("A is grater than B =", A >= B)
print("A is grater than B =", A > B)
print("A is grater than B =", A < B)
print("\t")

# Write a program to calculate the area of circle by taking Radius input

Radius = float(input("Enter the radius of circle\n"))
print(Radius)
pi=3.14
print(pi)
area = pi * pow(Radius,2)
print("Area of circle is",area)
print(f"{area:.2}")



