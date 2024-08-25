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
print("Comparision of Two numbers is", Compare)
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


