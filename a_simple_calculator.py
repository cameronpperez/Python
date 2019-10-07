# Creating a Calculator
# this lesson is about an example python project: a simple calculator
# each part explains a different section of the program.
# the first section is the overall menu. this keeps on accepting user input until the user enters "quit",
# so while loop is used.

# next part is getting the numbers the user wants to do something with. the code shows this for the addition section of
# the calculator. similar code would have to be written for the other sections.

while True:
    print("Options: ")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divid two numbers")
    print("Enter 'quit' to end the program")
    user_input = input("Enter: ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "subract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is " + result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is " + result)
    elif user_input == "divide":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("The answer is " + result)
    else:
        print("Unkown input")