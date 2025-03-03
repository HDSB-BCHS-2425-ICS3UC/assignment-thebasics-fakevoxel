import math

# find the discriminant of a quadratic, given the coefficients
def discriminant(a, b, c):
    return (b * b) - (4 * a * c)

# defining functions that apply the volume formulas of different shapes
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

# variables to be used for basic math
a = 1
b = 3

# defining arbitrary parameters for the shapes we want to calculate
# these will be set via user input soon
radius = 1
width = 5
height = 2

# demonstrating basic math
# --------------------------------

# addition
print(str(a) + " plus " + str(b) + " is " + str(a+b) + ".")
# subtraction
print(str(a) + " minus " + str(b) + " is " + str(a-b) + ".")
# multiplication
print(str(a) + " multiplied by " + str(b) + " is " + str(a*b) + ".")
# division
print(str(a) + " divided by " + str(b) + " is " + str(a/b) + ".")
# modulus
print(str(a) + " modulo " + str(b) + " is " + str(a%b) + ".")

# demonstrating the volume functions
# -----------------------------------

# cube
print("The area of a cube with side length " + str(width) + " is " + str(findVolumeOfCube(width)) + ".")
# sphere
print("The area of a sphere with radius " + str(radius) + " is " + str(findVolumeOfSphere(radius)) + ".")
# cone
print("The area of a cone with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCone(radius, height)) + ".")
# cylinder
print("The area of a cylinder with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCylinder(radius, height)) + ".")