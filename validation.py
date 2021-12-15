#1 ask user for pet name, store it in a variable
pet_name = input('enter your pet name:')
#2 use fn to get pet name length, store length in a new variable
pet_name_length = len(pet_name)
#3 validate - if-elif to print error messages if len is outside boundaries
if(pet_name_length == 0):
    print("you must enter something")
elif(pet_name_length <2):
    print("Your pet must have a name with more than 2 letters")
elif(pet_name_length >= 20):
    print("Enter a name that is less than or equal to 20 letters")

