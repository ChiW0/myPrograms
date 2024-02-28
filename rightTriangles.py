base = float(input('base of the triangle: '))
height = float(input('height of the triangle: '))

heightSqrd = float(height ** 2)
baseSqrd = float(base ** 2)

hypotenuseSqrd = baseSqrd + heightSqrd

hypotenuse = hypotenuseSqrd ** 0.5



print("The hypotenuse of the triangle with these dimensions is", hypotenuse)