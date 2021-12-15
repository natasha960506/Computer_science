#user input error - this throws an exception if a string is given by user 
#age =int(input()) 


#try-catch block
try:
    age = int(input("Enter your age:"))
    calculation = 10/age
except (ValueError, ZeroDivisionError) as error:
    print("please enter a valid")
    
