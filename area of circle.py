import math

# Function to calculate area of a circle given it's radius
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Set radius value of circle
radius_value = 3

# Call the function with the set radius
result = calculate_circle_area(radius_value)

# Print the result
print("The area of the circle is:", result)