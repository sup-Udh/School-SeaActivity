#2 q
# To perform the following operations according to the user’s choice using menu.
#a) Area of circle
#b) Area of rectangle
#c) Area of square
#d) Area of triangle
#e) Area of trapezoid
#f) Area of polygon
#g) Exit


x = input("the area of which shape do you want to find out (circle,square,rectangle, polygon)?")
if x == 'circle':
    y = int(input("enter the radius of the circle"))
    area = 3.14 * int(y) ** 2
    print("the area of the circle is:",area)
elif x == 'square':
    y = int(input("enter the side of the square"))
    area = y*y
    print("the area of the square is:",area)
elif x == 'rectangle':
    rect1 = int(input("enter the length of the rectangle"))
    rect2 = int(input("enter the width of the rectangle"))
    area = rect1*rect2
    print("the area of the rectangle is:",area)
elif x == 'triangle':
    y = int(input("enter the base of the triangle"))
    z = int(input("enter the height of the triangle"))
    area = 0.5*y*z
    print("the area of the triangle is:",area)
elif x == 'trapezoid':
    y = int(input("enter the base of the trapezoid"))
    z = int(input("enter the height of the trapezoid"))
    area =  0.5*(y+z)*z
    print("the area of the trapezoid is:",area)
elif x == 'polygon':
    y = int(input("enter the number of sides of the polygon"))
    z = int(input("enter the length of the side of the polygon"))
    area = 0.5*y*z
    print("the area of the polygon is:",area)
else:
    print("invalid input")




