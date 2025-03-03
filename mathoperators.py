import math

# here we define functions that apply the area formulas of different shapes
#--------------------------------------

# formula for area of a cube is width^3
def findAreaOfCube(width):
    return width * width * width

#formula for area of a sphere is (4/3)(pi)(radius^3)
def findAreaOfSphere(radius):
    return (4 / 3) * radius * radius * radius * math.pi

# defining arbitrary parameters for the shapes we want to calculate
# these will be set via user input soon
radius = 1
width = 5

print("The area of a cube with side length " + str(width) + " is " + str(findAreaOfCube(5)) + ".")


print("The area of a sphere with radius " + str(radius) + " is " + str(findAreaOfSphere(5)) + ".")