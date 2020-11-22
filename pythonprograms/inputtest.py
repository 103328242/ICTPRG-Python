# # valid = False
# # while not valid:
# #     number = input("Enter a positive integer: ")
# #     if number.isdigit():
# #         valid = True
# #         #print("Great!! The number",number, "is valid.")
# #     else:
# #         print("Please enter a positive number.")
# # print("Great!! The number",number, "is valid.")

# num = input("Enter a number: ")
# while num:
#     #num = input("Enter a number: ")
#     try:
#         num1 = int(num)
#         if num1 <= 0:
#             print("The entered number",num1,"is a negative number.")
#             break
#         elif num1 == str:
#             print("This is a string, please enter a valid number.")
#             break
#         # else:
#         #     print("Great!!Entered number",num1,"is valid.")
#         #     break
#     except Exception as e:
#         print(e)
# #print("Great!!Entered number",num1,"is valid.")
        
# Python program to validate an Ip address 
  
# re module provides support 
# for regular expressions 
import re 
  
# Make a regular expression 
# for validating an Ip-address 
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
      
# Define a function for 
# validate an Ip addess 
def check(Ip):  
    
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex, Ip)):  
        print(Ip," is Valid Ip address")  
          
    else:  
        print(Ip," is Invalid Ip address")  
      

# Driver Code  
if __name__ == '__main__' :  
      
    # Enter the Ip address 
    Ip = "192.168.0.1"
      
    # calling run function  
    check(Ip) 
  
    Ip = "110.234.52.124"
    check(Ip) 
  
    Ip = "366.1.2.2"
    check(Ip) 
