#Prompt the user to enter three numbers
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

#compute the average
average = (num1 + num2 + num3) / 3

#Display the result
print(f"The average of {num1}, {num2}, and {num3} is: {average}!")