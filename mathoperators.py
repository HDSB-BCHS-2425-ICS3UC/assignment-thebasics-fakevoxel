import math

# here we define functions that apply the area formulas of different shapes
#--------------------------------------

# formula for area of a cube is width^3
def findVolumeOfCube(width):
    return width * width * width

# formula for area of a sphere is (4/3)(pi)(radius^3)
def findVolumeOfSphere(radius):
    return (4 / 3) * radius * radius * radius * math.pi

# formula for area of a cone is (1/3)(pi)(radius^2)(height)
def findVolumeOfCone(radius, height):
    return (1/3) * math.pi * radius * radius * height

# formula for area of a cylinder is (pi)(height)(radius^2)
def findVolumeOfCylinder(radius, height):
    return math.pi * radius * radius * height

# defining arbitrary parameters for the shapes we want to calculate
# these will be set via user input soon
radius = 1
width = 5
height = 2

print("The area of a cube with side length " + str(width) + " is " + str(findVolumeOfCube(width)) + ".")

print("The area of a sphere with radius " + str(radius) + " is " + str(findVolumeOfSphere(radius)) + ".")

print("The area of a cone with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCone(radius, height)) + ".")

print("The area of a cylinder with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCylinder(radius, height)) + ".")