import math

# Function calculating volume of a sphere given it's radius
def calculate_volume_sphere(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume

# Set radius value
radius_value = 5

# Calling function with set radius value
result = calculate_volume_sphere(radius_value)

# Print result
print("The volume of the sphere is:", result)