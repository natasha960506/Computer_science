#get and store user input
#name = input("Enter your name: ")

#output the user input on the screen
#print("Good morning", name)

#ask user to enter a number (integer)
#save it in a variable called "number"
number = int(input("Enter a number:"))

#defining a new function called "get_square"
#pass input to a function that does math 
def get_square (number):
    return number * number

#call the square function, pass "number" as argument
#save the result in a variable called "square"
#print the "square" variable on screen
square = get_square(number)
print(square) 

