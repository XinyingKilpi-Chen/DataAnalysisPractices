#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    '''Choose a shape (triangle, rectangle, circle): triangle
    Give base of the triangle: 20
    Give height of the triangle: 5
    The area is 50.000000
    Choose a shape (triangle, rectangle, circle): rectangel
    Unknown shape!
    Choose a shape (triangle, rectangle, circle): rectangle
    Give width of the rectangle: 20
    Give height of the rectangle: 4
    The area is 80.000000
    Choose a shape (triangle, rectangle, circle): circle
    Give radius of the circle: 10
    The area is 314.159265
    Choose a shape (triangle, rectangle, circle): '''
    i=1
    while i:
        
        shape=input("Choose a shape (triangle, rectangle, circle): ")
        if shape=='':
            break
        elif shape=="triangle":
            base=float(input("Give base of the triangle: "))
            height=float(input("Give height of the triangle: "))
            area=base*height/2
            print(f"The area is {area}")
        elif shape=="rectangle":
            width=float(input("Give width of the rectangle: "))
            height=float(input("Give height of the rectangle: "))                
            
            area=width*height
            print(f"The area is {area}")
        elif shape=="circle":
            radius=float(input("Give radius of the circle: "))                
            area=math.pi*radius**2
            print(f"The area is {area:.{6}f}")
        else:
            print("Unknown shape!")
        
    




if __name__ == "__main__":
    main()
