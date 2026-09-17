names = []
number_of_names = eval(input("Enter the number of names: "))
for i in range(number_of_names):
    names.append(input("Enter name: "))
count = 0
while count < number_of_names:
    print(f"Kill {names[count]}")
    count += 1