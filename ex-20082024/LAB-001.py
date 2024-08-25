
# Grade Calculater
#  write a PROGRAM that calculates and displays the letters grade
# for a given numerical score (e.f,A,B,C,D,E,F)
# A:90-100
# B:80_89
# C:70-79
# D:60-90
# F: 0-59

Marks_value = float(input("enter the Marks obtained "))
print(Marks_value)

if 90 <= Marks_value <= 100:
    print("The Grade obtained based on marks obtained is ", "A")

elif 80 <= Marks_value <= 90:
    print("The Grade Obtained based on marks obtained is", "B")

elif 70 <= Marks_value <= 79:
    print("The Grade obtained based on marks obtained is","C")

elif 60 <= Marks_value <= 90:
    print("The Grade obtained based on Marks obtained is ", "D")
elif 0 <= Marks_value <= 59:
    print("The Grade obtained based on Marks Obtained is", "F")

else:
    print("Invalied marks please enter the value between 0 to 100")