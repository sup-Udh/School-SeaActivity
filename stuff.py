
#  Read the number of sides the polygon has and display which polygon it is.
#  If the number of sides is not 3, 4, 5, or 6, display an error message.



input_sides = int(input("Enter the number of sides: "))


if input_sides == 3:
    print("Triangle")
elif input_sides == 4:
    print("Quadrilateral")
elif input_sides == 5:
    print("Pentagon")
elif input_sides == 6:
    print("Hexagon")
else:
    print("Error")
