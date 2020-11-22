# while True:
#     try:
#         # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
#         InputNumber = int(input("Please enter a number: "))
#     except ValueError:
#         print("Sorry, Thats not a what I expect!!.")
#         #better try again... Return to the start of the loop
#         continue
#     else:
#         #age was successfully parsed!
#         #we're ready to exit the loop.
#         break
# if InputNumber >= 20: 
#     print("A valid number!: ", InputNumber)
# else:
#     print("Sorry Try again.")

##The below works!!
# from itertools import chain, repeat

# prompts = chain(["Enter a number: "], repeat("Not a number! Try again: "))
# replies = map(input, prompts)
# valid_response = next(filter(str.isdigit, replies))
# print("valid Number!!\n", valid_response)

# def get_non_negative_int(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#         except ValueError:
#             print("Sorry, I didn't understand that.")
#             continue

#         if value < 0:
#             print("Sorry, your response must not be negative.")
#             continue
#         else:
#             break
#     return value

# age = get_non_negative_int("Please enter your age: ")
# kids = get_non_negative_int("Please enter the number of children you have: ")
# salary = get_non_negative_int("Please enter your yearly earnings, in dollars: ")
# number = None
# while number is None:
#     input_value = input("Please enter a number: ")
#     try:
#         # try and convert the string input to a number
#         number = int(input_value)
#     except ValueError:
#         # tell the user off
#         print("{input} is not a number, please enter a number only".format(input=input_value))
##below given is my helpcode
# age = None
# while age is None:
#     input_value = input("Please enter your age: ")
#     try:
#         # try and convert the string input to a number
#         age = int(input_value)
#     except ValueError:
#         # tell the user off
#         print("{input} is not a number, please enter a number only".format(input=input_value))
# if age <= 0:
#     print("You are able to vote in the United States!")
# else:
#     print("You are not able to vote in the United States.")

input_value = None
while input_value is None:
    
    #while True:
    input_value = input("Please enter a positive number: ")
    try:
        # try and convert the string input to a number
        InputNumber = int(input_value)
    except ValueError:
        # tell the user off
        #print("{input} is not a number, please enter positive number only".format(input=InputNumber))
        print(InputNumber, " is not a number, please use positive numbers only")

    if InputNumber < 0:
        #print("Sorry, {input} is a negative number which is invalid. Please try again".format(input=InputNumber))
        print(InputNumber, " is a negative number, please use positive numbers only")
        continue
    else:
        #print("Yippeee!!! {input} is a valid number!!".format(input=InputNumber))
        print("Yippeee!!!", InputNumber ," is a valid number!!")
        #break
