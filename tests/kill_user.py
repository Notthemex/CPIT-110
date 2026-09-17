names = []
number_of_names = eval(input("Enter the number of names: "))
for i in range(number_of_names):
    names.append(input("Enter name: "))
print(f"Kill {", " .join(names)}")