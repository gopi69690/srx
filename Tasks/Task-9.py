### Task #9
"""
✅ FizzBuzz Test:

Write a program that prints numbers from 1 to 100. # Loop For

However, for multiples of 3, print "Fizz" instead of the number, and

for multiples of 5, print "Buzz."

For numbers that are multiples of both 3 and 5, print "FizzBuzz."
"""
Num=int(input("enter the number between 1 to 100"))
print(Num)
if Num %5==0 and Num %3==0:
    print("FIZZ BUZZ")
elif Num %3==0:
    print("FIZZ")
elif Num %5==0:
    print("BUZZ")
else:
    print("Enter the valid number")