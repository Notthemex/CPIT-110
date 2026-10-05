#ask user to enter the amount of seconds
seconds = eval(input("Enter an integer for seconds: "))

#calculate the amount of minutes by using floor division with the seconds and dividing it by 60
minutes = seconds // 60

#calculate the remaining seconds by using the modulo to get the remainder
remaining_seconds = seconds % 60

#print the output
print(f"{seconds} is {minutes} minutes and {remaining_seconds} seconds.")