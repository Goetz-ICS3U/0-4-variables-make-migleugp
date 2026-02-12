"""
author: Miguel Gonzalez
date: February 12, 2026
Make Variables
"""

# Input

circle_radius = int(input("The radius of the circle:"))
rectangle_length = int(input("The length of the rectangle:"))
rectangle_width = int(input("The width of the rectangle:"))
octagon_length = int(input("A side length of the octagon:"))

import math
pi = math.pi
s = math.sqrt

# Processing
area_circle = (circle_radius**2) * pi
area_rectangle = (rectangle_width*rectangle_length)
area_octagon = 2 * (1 + s(2)) * (octagon_length**2)

perimeter_circle = (circle_radius*2*pi)
perimeter_rectangle = (2*rectangle_length) + (2*rectangle_width)
perimeter_octagon = (8*octagon_length)
# Output

print(f"The circle has an area of {area_circle} and a perimeter of {perimeter_circle}")
print(f"The rectangle has an area of {area_rectangle} and a perimeter of {perimeter_rectangle}")
print(f"The octagon has an area of {area_octagon} and a perimeter of {perimeter_octagon}")