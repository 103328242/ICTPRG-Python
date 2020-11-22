valid = False
while not valid:
    number = input("Enter a positive integer: ")
    if number.isdigit():
        valid = True
    else:
        print("Please use a valid number.")
print("Great!! The number",number, "is valid.")    