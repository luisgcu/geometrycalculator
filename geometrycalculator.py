# Filename: geometrycalculator.py
# Author: Luis Guerrero
# Date: September 17, 2022
# Program Description: Given information about a circle, rectangle and a triangle, 
# calculate the area of the shape from the information supplied. 
# Write a Python program that asks the user to input the required information 
# for a shape and then calculates the area of the shape.
from math import pi


validSelection =False
print("\nGeometry Calculatror\n")
print("1.  Calculate the Area of a Circle")
print("2.  Calculate the Area of a Rectangle")
print("3.  Calculate the Area of a Triangle")
print("4.  Quit")

userSelection = int(input("Enter your choice (1 - 4): "))
# while userSelection < 1 or   userSelection > 4 :    
#     userSelection = int(input("Enter your choice (1 - 4): "))

if userSelection <=0 or userSelection >4  :
    print(userSelection,"user choice not valid")
    int(input("Enter your choice (1 - 4): "))
else:
    validSelection =True

if   validSelection : 
    #Area of circle calculation   
    if userSelection == 1 :
        #Calculate the Area of a Circle
        radius = float(input("Enter then radius of the circle in inches: "))
        if radius <=0   :   
            print(radius,"is not valid\n")     
            radius = float(input("Enter then radius of the circle in inches: "))
        if radius >0 :
            circleArea=pi*radius**2
            print(f'Area of the circle is:  {circleArea:.2f}  inches square ') 


    if userSelection ==2:
        #Calculate the Area of a Rectangle
        rectangleLength = float(input("Enter then length of the rectangle in inches: "))
        if rectangleLength <=0   :   
            print(rectangleLength,"is not valid\n")     
            rectangleLength = float(input("Enter then length of the rectangle in inches: "))

        rectangleWidth = float(input("Enter then Width of the rectangle in inches: "))
        if rectangleWidth <=0   :   
            print(rectangleWidth,"is not valid\n")     
            rectangleWidth = float(input("Enter then Width of the rectangle in inches: "))

        if rectangleLength and rectangleWidth  >0 :
            rectangleArea=rectangleLength*rectangleWidth
            print(f'Area of the Rectangle is :  {rectangleArea:.2f}  inches square ') 

    if userSelection ==3:
        #Calculate the Area of a triangle
        triangleHeight = float(input("Enter then Height of the triangle in inches: "))
        if triangleHeight <=0   :   
            print(triangleHeight,"is not valid\n")     
            triangleHeight = float(input("Enter then Height of the triangle in inches: "))

        triangleBase = float(input("Enter then base length of the triangle in inches: "))
        if triangleBase <=0   :   
            print(triangleBase,"is not valid\n")     
            triangleBase = float(input("Enter then base length of the triangle in inches: "))

        if triangleHeight and triangleBase  >0 :
            triangleArea=triangleHeight*triangleBase/2
            print(f'Area of the triangle is :  {triangleArea:.2f}  inches square ')
    if userSelection ==4:
        print("\nProgram END\n")

    #     #Calculate the Area of a Circle
    # if userSelection=3:
    #     #Calculate the Area of a Circle
    # if userSelection=4:
    #     #QUIT







