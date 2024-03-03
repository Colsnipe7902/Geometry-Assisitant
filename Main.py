welcome_banner = """Welcome to geometry assisitant"""
print(welcome_banner)
pi = 3.14
radius = float(input('Enter the radius:'))
circle_perimeter = 2 * pi * radius
print(f"Circle Perimeter:{circle_perimeter}")
circle_area = pi * radius * radius
print(f"Circle Area:{circle_area}")
leg1 = float(input("What is the length of the leg:"))
leg2 = float(input("What is the length of the leg:"))
triangle_area = (leg1 * leg2) / 2
print(f"Triangle area:{triangle_area}")


square = float(input("What is the width: "))
square2 = float(input("What is the length: "))
square_perimeter = 2 * (square + square2)
square_area = square * square2
print(f"Square perimeter: {square_perimeter}")
print(f"Square area: {square_area}")
