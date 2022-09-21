#Author: Kriditty Ikhlaas Lawang
#Program Name: Ikhlaas — Calculator.py

#License: GNU GPLv3.0
#Status: Release
#Version: 1.0
#Release Date: 13-09-2022
#Description: Basic Python console/Shell calculator using two whole number inputs and returning the output

#Copyright (C) 2022 Kridtity Lawang

#Define the 5 maths methods modes
math_modes = (1, 2, 3, 4, 5)

#Define the main menu function
def menu():
    print(10*"-" + "The Calculator Program" + 10*"-" + "\n")
    mode = int(input("Calculator menu modes:\n"
                 "    l: Addition\n"
                 "    2: Subtraction\n"
                 "    3: Multiplication\n"
                 "    4: Division\n"
                 "    5: Powers\n"
                 "    6: Exit\n"
                 "Choose a mode and enter the number here: "))

    return mode

#Define check for 42 function
def check_for_42(result):
    if result == 42:
        print("42! That is the answer to the Ultimate Question of Life, the Universe, and Everything!")
    else:
        pass

#Define input reception function
def receive_input():
    print("")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("")

    return num1, num2

#Define the addition function
def addition(num1, num2):
    result = num1 + num2

    return result

#Define the subtraction function
def subtraction(num1, num2):
    result = num1 - num2

    return result

#Define the multiplication function
def multiplication(num1, num2):
    result = num1 * num2

    return result

#Define the division function
def division(num1, num2):
    result = num1 / num2

    return result

#Define the powers function
def powers(num1, num2):
    result = num1 ** num2

    return result

#Initialise main loop (improvised forever loop)
while True:
    #Call menu function to printm menu and get mode input
    mode = menu()

    #If mode input is in list of maths modes, proceed to calculation. Or if mode is quit then print goodbye message and leave. Else, return error (error handling)
    if mode in math_modes:
        #Addition selection
        if mode == 1:
            operands = receive_input()
            result = addition(operands[0], operands[1])
            print("Answer: {} + {} = {}\n".format(operands[0], operands[1], result))

            check_for_42(result)
        #Subtraction selection
        elif mode == 2:
            operands = receive_input()
            result = subtraction(operands[0], operands[1])
            print("Answer: {} - {} = {}\n".format(operands[0], operands[1], result))

            check_for_42(result)
        #Multiplication selection
        elif mode == 3:
            operands = receive_input()
            result = multiplication(operands[0], operands[1])
            print("Answer: {} * {} = {}\n".format(operands[0], operands[1], result))

            check_for_42(result)
        #Division selection
        elif mode == 4:
            operands = receive_input()
            result = division(operands[0], operands[1])
            print("Answer: {} / {} = {}\n".format(operands[0], operands[1], result))

            check_for_42(result)
        #Powers selection
        elif mode == 5:
            operands = receive_input()
            result = powers(operands[0], operands[1])
            print("Answer: {} ^ {} = {}\n".format(operands[0], operands[1], result))

            check_for_42(result)
        #Else catch error
        else:
            print("Error in maths operation.")
            continue

    #Quit if mode = 6 (quit mode)
    elif mode == 6:
        print("Thank you, Goodbye!")
        quit()

    #Else catch error   
    else:
        print("Number outside range or other invalid input. Please choose a valid input.\n")
        continue
