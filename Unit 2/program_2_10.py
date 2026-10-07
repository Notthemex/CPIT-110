#ask the user for the first point, x1 and y1
x1, y1 = eval(input("Enter the values for x1 and y1 seperated by a comma: "))

#ask the user for the first point, x2 and y2
x2, y2 = eval(input("Enter the values for x2 and y2 seperated by a comma: "))

#computer the distance
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

#display the result
print(f"The distance between the points ({x1, y1}) and ({x2, y2}) is {distance}")