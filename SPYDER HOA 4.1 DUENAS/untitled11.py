import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    print("Discriminant:", discriminant)

    if discriminant < 0:
        print("No real solutions")
        return None, None
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

r1, r2 = quadratic_solver(a, b, c)

# Display results
if r1 is not None:
    print("Root 1:", r1)
    print("Root 2:", r2)
