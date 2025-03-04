import math
 
# Message from the developer:

# This script is written how I usually like to write console applications, 
# where there is a function that records the users input and then calls other functions to handle commands.
# This is done through a large if/elif statement in the main logic function.
# 
# There is one function for each command, one for the main command logic ( runMainPrompt() ), 
# plus whatever helper functions are necessary.

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

# the MAIN LOGIC FUNCTION
# allows the user to input a command and then runs the command based on input
# all commands will go here after running
#----------------------------------
def runMainPrompt():

    # write a prompt for the user
    print("")
    print("----------------------------------")
    print("What operation would you like to run? Type (help) for all possible commands.")
    print("Type (demo) for a demonstration of variable types.")

    # record the user's input
    userInput = input()

    # checking for each available command
    if (userInput == "help"):
        print("")
        runHelpCommand()
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

# the help command, which just shows all other commands and what they do
#----------------------------------
def runHelpCommand():
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

# the addition command
#----------------------------------
def runAddCommand():
    # get the variables to be used from the user
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    # nicely print the result to the user
    print(str(a) + " + " + str(b) + " is " + str(a+b) + ".")

    # going back to the main command logic
    runMainPrompt()

# the subtraction command
#----------------------------------
def runSubtractCommand():
    # get the variables to be used from the user
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    # nicely print the result to the user
    print(str(a) + " - " + str(b) + " is " + str(a-b) + ".")

    # going back to the main command logic
    runMainPrompt()

# the multiplication command
#----------------------------------
def runMultiplyCommand():
    # get the variables to be used from the user
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    # nicely print the result to the user
    print(str(a) + " * " + str(b) + " is " + str(a*b) + ".")

    # going back to the main command logic
    runMainPrompt()

# the division command
#----------------------------------
def runDivideCommand():
    # get the variables to be used from the user
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    # nicely print the result to the user
    print(str(a) + " / " + str(b) + " is " + str(a/b) + ".")

    # going back to the main command logic
    runMainPrompt()

# the modulus command
#----------------------------------
def runModulusCommand():
    # get the variables to be used from the user
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))

    # nicely print the result to the user
    print(str(a) + " % " + str(b) + " is " + str(a%b) + ".")
    
    # going back to the main command logic
    runMainPrompt()

# the discriminant command, which allows you to input coefficients of a quadratic and get the discriminant
#----------------------------------
def runDiscriminantCommand():
    # get the coefficients of the quadratic from the user
    a = float(input("Enter an (a) value then press enter... "))
    b = float(input("Enter a (b) value then press enter... "))
    c = float(input("Enter a (c) value then press enter... "))

    # nicely print the result (discriminant) to the user
    print("The discriminant of a quadratic with coefficients of a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " is " + str(discriminant(a, b, c)))

    # going back to the main command logic
    runMainPrompt()

# the volume-cube command, which allows you to input values to calculate volume of a cube
#----------------------------------
def runVolumeCubeCommand():
    # get the width value from the user
    width = float(input("Enter a (width) value then press enter... "))

    # nicely print the result (volume) to the user
    print("The area of a cube with side length " + str(width) + " is " + str(findVolumeOfCube(width)) + ".")

    # going back to the main command logic
    runMainPrompt()

# the volume-sphere command, which allows you to input values to calculate volume of a sphere
#----------------------------------
def runVolumeSphereCommand():
    # get the radius value from the user
    radius = float(input("Enter a (radius) value then press enter... "))

    # nicely print the result (volume) to the user
    print("The area of a sphere with radius " + str(radius) + " is " + str(findVolumeOfSphere(radius)) + ".")

    # going back to the main command logic
    runMainPrompt()

# the volume-cone command, which allows you to input values to calculate volume of a cone
#----------------------------------
def runVolumeConeCommand():
    # get the radius and height value from the user
    radius = float(input("Enter a (radius) value then press enter... "))
    height = float(input("Enter a (height) value then press enter... "))

    # nicely print the result (volume) to the user
    print("The area of a cone with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCone(radius, height)) + ".")

    # going back to the main command logic
    runMainPrompt()

# the volume-cylinder command, which allows you to input values to calculate volume of a cylinder
#----------------------------------
def runVolumeCylinderCommand():
    # get the radius and height value from the user
    radius = float(input("Enter a (radius) value then press enter... "))
    height = float(input("Enter a (height) value then press enter... "))

    # nicely print the result (volume) to the user
    print("The area of a cylinder with radius " + str(radius) + " and height " + str(height) + " is " + str(findVolumeOfCylinder(radius, height)) + ".")

    # going back to the main command logic
    runMainPrompt()

# the demo command, which displays basic data types to the terminal
#----------------------------------
def runDemoCommand():

    # creating one variable for each data type
    intExample = 4
    floatExample = 4.2
    doubleExample = 3.5
    stringExample = "this is a scentence"
    charExample = 'a'  
    booleanExample = True

    # displaying those variables on the terminal
    print("There are six variable types that we work with in this course. They are: ")
    print("")
    print("Integers (whole numbers). Example: " + str(intExample))
    print("Floats (decimal numbers). Example: " + str(floatExample))
    print("Doubles (decimal numbers). Note: Python just makes these floats. Example: " + str(doubleExample))
    print("Strings (a bunch of characters). Example: " + stringExample)
    print("Chars (just one character). Example: " + str(charExample))
    print("Booleans (true/false value). Example: " + str(booleanExample))

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