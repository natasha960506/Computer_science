#1 - get name of resturant 
resturant_name = input("Enter a resturant name: ")
print(resturant_name)
#2 - get length
resturant_name_length = len(resturant_name)
print(resturant_name_length)
#3 - validation 
if(resturant_name_length == 0):
    print("You must enter something")
elif(resturant_name_length < 5):
    print("You must enter a name with more than five letters")
elif(resturant_name_length > 55):
    print("You must enter a name with less than 25 letters")