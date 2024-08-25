"""
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.

"""

X = float(input("enter the value of X"))
Y = float(input("enter the value of Y"))
Z = float(input("enter the value of Z"))

if X==Y and Y==X and X==Z and Z==X and Y==Z and Z==Y:
    print("Based on the Input values it is an equilateral triangle ""\n",X,Y,Z)
elif X!=Y and Y!=X and X!=Z and Z!=X and Y!=Z and Z!=Y:
    print("Based on the Input values it is an scalene triangle""\n",X,Y,Z)
elif X==Y or Y!=X or X==Z or Z!=X or Y==Z or Z!=Y:
    print("Based on the Input values it is an isosceles triangle""\n",X,Y,Z)

else:
    print("Please enter the valid inputs")
