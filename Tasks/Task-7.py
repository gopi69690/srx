#Create a program that determines whether a given year is a leap year.A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.Create a program that determines whether a given year is a leap year.
#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400
#Use an if-else statement to make this determination.

Year=int(input("Enter the year which you want to check if its leap year"))
print(Year)
if Year % 4 == 0 or Year % 100 == 0 or Year % 400 == 0:
    print("The entered year is Leap year", Year)
else:
    print("The entered year is not leap Year")
