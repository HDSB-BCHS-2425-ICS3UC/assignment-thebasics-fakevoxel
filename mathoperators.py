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
    print("")
    print("----------------------------------")
    print("What operation would you like to run? Type (help) for all possible commands.")
    print("Type (demo) for a demonstration of variable types.")

    userInput = input()

    if (userInput == "help"):
        print("")
        print("Here is a list of all possible commands:")
        print("")
        print("(add) - add two values together")
        print("(subtract) - subtract two values")
        print("(multiply) - multiply two values")
        print("(divide) - divide two values")
        print("(modulus) - find the remainder, from one value divided by another")
        print("(discriminant) - find the discriminant of a quadratic with supplied coefficients")
        print("(volume-cube) - find the volume of a cube with a supplied width")
        print("(volume-sphere) - find the volume of a sphere with a supplied radius")
        print("(volume-cone) - find the volume of a cone with supplied radius and height")
        print("(volume-cylinder) - find the volume of a cylinder with supplied radius and height")
        runMainPrompt()
    elif (userInput == "add"):
        print("")
        runAddCommand()
    elif (userInput == "subtract"):
        print("")
        runSubtractCommand()
    elif (userInput == "multiply"):
        print("")
        runMultiplyCommand()
    elif (userInput == "divide"):
        print("")
        runDivideCommand()
    elif (userInput == "discriminant"):
        print("")
        runDiscriminantCommand()
    elif (userInput == "volume-cube"):
        print("")
        runVolumeCubeCommand()
    elif (userInput == "volume-sphere"):
        print("")
        runVolumeSphereCommand()
    elif (userInput == "volume-cone"):
        print("")
        runVolumeConeCommand()
    elif (userInput == "volume-cylinder"):
        print("")
        runVolumeCylinderCommand()
    elif (userInput == "demo"):
        print("")
        runDemoCommand()

# addition
def runAddCommand():
    # variables to be used for basic math
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    print(str(a) + " + " + str(b) + " is " + str(a+b) + ".")
    # going back to the main command logic
    runMainPrompt()

# subtraction
def runSubtractCommand():
    # variables to be used for basic math
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    print(str(a) + " - " + str(b) + " is " + str(a-b) + ".")
    # going back to the main command logic
    runMainPrompt()

# multiplication
def runMultiplyCommand():
    # variables to be used for basic math
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    print(str(a) + " * " + str(b) + " is " + str(a*b) + ".")
    # going back to the main command logic
    runMainPrompt()

# division
def runDivideCommand():
    # variables to be used for basic math
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    print(str(a) + " / " + str(b) + " is " + str(a/b) + ".")
    # going back to the main command logic
    runMainPrompt()

# modulus
def runModulusCommand():
    # variables to be used for basic math
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    print(str(a) + " % " + str(b) + " is " + str(a%b) + ".")
    # going back to the main command logic
    runMainPrompt()

# discriminant
def runDiscriminantCommand():
    # coefficients of the quadratic
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))
    c = float(input("Enter a (c) value then press enter... "))

    print("The discriminant of a quadratic with coefficients of a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " is " + str(discriminant(a, b, c)))
    # going back to the main command logic
    runMainPrompt()

def runVolumeCubeCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    width = float(input("Enter a (width) value then press enter... "))

    # cube
    print("The area of a cube with side length " + str(width) + " is " + str(findVolumeOfCube(width)) + ".")
    # going back to the main command logic
    runMainPrompt()

def runVolumeSphereCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    radius = float(input("Enter a (radius) value then press enter... "))

    # sphere
    print("The area of a sphere with radius " + str(radius) + " is " + str(findVolumeOfSphere(radius)) + ".")
    # going back to the main command logic
    runMainPrompt()

def runVolumeConeCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    radius = float(input("Enter a (radius) value then press enter... "))
    height = float(input("Enter a (height) value then press enter... "))

    # cone
    print("The area of a cone with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCone(radius, height)) + ".")
    # going back to the main command logic
    runMainPrompt()

def runVolumeCylinderCommand():
    # defining arbitrary parameters for the shapes we want to calculate
    radius = float(input("Enter a (radius) value then press enter... "))
    height = float(input("Enter a (height) value then press enter... "))

    # cylinder
    print("The area of a cylinder with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCylinder(radius, height)) + ".")
    # going back to the main command logic
    runMainPrompt()

def runDemoCommand():
    intExample = 4
    floatExample = 4.2
    doubleExample = 3.5
    stringExample = "this is a scentence"
    charExample = 'a'  
    booleanExample = True

    print("There are six variable types that we work with in this course. They are: ")
    print("")
    print("Integers. Example: " + str(intExample))
    print("Floats. Example: " + str(floatExample))
    print("Doubles. Note: Python just makes these floats. Example: " + str(doubleExample))
    print("Strings. Example: " + stringExample)
    print("Chars. Example: " + str(charExample))
    print("Booleans. Example: " + str(booleanExample))

    # going back to the main command logic
    runMainPrompt()

# ===================================================
# CODE FOR HANDLING CONSOLE INTERACTIONS:
# ===================================================

# introductory message
#----------------------------------

print("")
print("")
print("Welcome user!")
print("This is a script that demonstrates basic arithmetic and geometry.")
print("You will be prompted to select a calculation that you wish to complete, and then prompted for values.")
print("One all values are entered you will receive your result.")

# call to the function that runs the main command logic
runMainPrompt()