import math

# ===================================================
# HELPER FUNCTIONS:
# ===================================================

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

# functions for handling commands
# ----------------------------------

def runMainPrompt():
    print("----------------------------------")
    print("What operation would you like to run? Type (help) for all possible commands.")

    userInput = input()

    if (userInput == "help"):
        print("Here is a list of all possible commands:")
        print("")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        print("modulus")
        print("discriminant")
        print("volume-cube")
        print("volume-sphere")
        print("volume-cone")
        print("volume-cylinder")
        print("")
        runMainPrompt()
    elif (userInput == "add"):
        runAddCommand()
    elif (userInput == "subtract"):
        runSubtractCommand()
    elif (userInput == "multiply"):
        runMultiplyCommand()
    elif (userInput == "divide"):
        runDivideCommand()
    elif (userInput == "discriminant"):
        runDiscriminantCommand()
    elif (userInput == "volume-cube"):
        runVolumeCubeCommand()
    elif (userInput == "volume-sphere"):
        runVolumeSphereCommand()
    elif (userInput == "volume-cone"):
        runVolumeConeCommand()
    elif (userInput == "volume-cylinder"):
        runVolumeCylinderCommand()

# addition
def runAddCommand():
    # variables to be used for basic math
    a = float(input("Enter a value then press enter... "))
    b = float(input("Enter b value then press enter... "))

    
    print(str(a) + " plus " + str(b) + " is " + str(a+b) + ".")
    runMainPrompt()

# subtraction
def runSubtractCommand():
    # variables to be used for basic math
    a = float(input("Enter a value then press enter... "))
    b = float(input("Enter b value then press enter... "))

    print(str(a) + " minus " + str(b) + " is " + str(a-b) + ".")
    runMainPrompt()

# multiplication
def runMultiplyCommand():
    # variables to be used for basic math
    a = float(input("Enter a value then press enter... "))
    b = float(input("Enter b value then press enter... "))

    print(str(a) + " multiplied by " + str(b) + " is " + str(a*b) + ".")
    runMainPrompt()

# division
def runDivideCommand():
    # variables to be used for basic math
    a = float(input("Enter a value then press enter... "))
    b = float(input("Enter b value then press enter... "))

    print(str(a) + " divided by " + str(b) + " is " + str(a/b) + ".")
    runMainPrompt()

# modulus
def runModulusCommand():
    # variables to be used for basic math
    a = float(input("Enter a value then press enter... "))
    b = float(input("Enter b value then press enter... "))

    print(str(a) + " modulo " + str(b) + " is " + str(a%b) + ".")
    runMainPrompt()

# discriminant
def runDiscriminantCommand():
    # coefficients of the quadratic
    a = float(input("Enter a value then press enter... "))
    b = float(input("Enter b value then press enter... "))
    c = float(input("Enter c value then press enter... "))

    print("The discriminant of a quadratic with coefficients of a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " is " + str(discriminant(a, b, c)))
    runMainPrompt()

def runVolumeCubeCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    width = float(input("Enter width value then press enter... "))

    # cube
    print("The area of a cube with side length " + str(width) + " is " + str(findVolumeOfCube(width)) + ".")
    runMainPrompt()

def runVolumeSphereCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    radius = float(input("Enter radius value then press enter... "))

    # sphere
    print("The area of a sphere with radius " + str(radius) + " is " + str(findVolumeOfSphere(radius)) + ".")
    runMainPrompt()

def runVolumeConeCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    radius = float(input("Enter radius value then press enter... "))
    height = float(input("Enter height value then press enter... "))

    # cone
    print("The area of a cone with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCone(radius, height)) + ".")
    runMainPrompt()

def runVolumeCylinderCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    radius = float(input("Enter radius value then press enter... "))
    height = float(input("Enter height value then press enter... "))

    # cylinder
    print("The area of a cylinder with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCylinder(radius, height)) + ".")
    runMainPrompt()

# ===================================================
# CODE FOR HANDLING CONSOLE INTERACTIONS:
# ===================================================

# introductory message
#----------------------------------

print("Welcome user! This is a script that demonstrates basic arithmetic and geometry.")
print("You will be prompted to select a calculation that you wish to complete, and then prompted for values.")
print("One all values are entered you will receive your result.")
runMainPrompt()