# Declaration

first_number = 0  
second_number = 0
opreation = ""
result = 0


# Take Input
first_number = int(input("Please enter the 1st number: "))  # "10" -> 10
second_number = int(input("Please enter the 2nd number: "))  # "20" -> 20
opreation = input("Please enter one of + - * or /: ")

# Process the Input 
if opreation == "+":
    result = first_number + second_number
elif opreation == "-":
    result = first_number - second_number
elif opreation == "*":
    result = first_number * second_number
elif opreation == "/": #or we can use this code elif opreation == "/": and second_number > 0:
    if second_number > 0: # by deleting this code 
     result = first_number / second_number
else:
   print("[WARN]opreation not supported!")

# Output
print("Result is: ", result, "!!!")
print("End of Script")
