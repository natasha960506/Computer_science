#programs make decisions based on control logic (control flow)
student_gread = 99

if student_gread > 90:
    print("Your gread is A")
elif student_gread < 90 and student_gread > 80:
    print ("Your gread is a B") 
elif student_gread < 80 and student_gread > 70 :
    print("Your gread is a C") 
else: 
    print ("Your gread is a D or F")

#write a program using if-elif-else that....
#looks at a variable for temperature = 20C
#if temperature is above 30 C, print it's hot
#elif temperature is above 10 C, but below 30 C, print it's warm
#elif temperature is below 10 C, print it's cold
#else print "bring an umbrella just in case"

temperature = 20 
if temperature > 30:
    print("it's hot") 
elif temperature
    