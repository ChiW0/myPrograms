import math


# Function to calculate area of a circle given it's radius
def calculateCircleArea(radius):
    try:
        radius = float(radius)
        area = math.pi * radius ** 2
        return area
    except ValueError:
        return "Invalid input."


