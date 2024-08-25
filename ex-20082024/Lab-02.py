# write a program for club entry logic using if, else

age= int(input("enter the age "))
print(age)
if age >= 18:
    print("can go to club as age is 18+")
else:
    print("entry denied due to age is less that 18")

# write a program to find the max of 3 numbers using if ,elif, else

X = float(input("enter the value of X"))
Y = float(input("enter the value of Y"))
Z = float(input("enter the value of Z"))
print(X,Y,Z)
if X > Y and X > Z:
    print("The MAX number is X")
elif Y > X and Y > Z:
    print("the MAX Number is Y")
else:
    print("The MAX Number is Z")

