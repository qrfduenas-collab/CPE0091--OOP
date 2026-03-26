import math

def projectile_calc(velocity, angle):
    gravity = 9.81

    # convert the degrees to angle
    theta_rad = math.radians(angle)

    distance = (velocity ** 2 * math.sin(2 * theta_rad)) / gravity

    max_height = (velocity ** 2 * (math.sin(theta_rad) ** 2)) / (2 * gravity)

    return distance, max_height

# for example
d, h = projectile_calc(25.0, 30.0)

print("Range:", d)
print("Maximum Height:", h)
