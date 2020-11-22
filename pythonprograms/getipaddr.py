# import socket

# def valid_ip(address):
#     try: 
#         socket.inet_aton(address)
#         return True
#         #print("Your IP address: "+address+"is Valid")
#     except:
#         return False

# print (valid_ip('10.10.20.30'))
# print (valid_ip('999.10.20.30'))
# print (valid_ip('gibberish'))

# import re

# # pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
# pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
# hostIP = input("Enter an ip address: ")
# test = pat.match(hostIP)
# if test:
#    print ("Acceptable ip address")
# else:
#    print ("Unacceptable ip address")
# import re

# def ipcheck():

# # 1.Validate the ip adderess
#     ipaddr = input('Enter the ip:')
#     flag = 0

#     pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
#     match = re.match(pattern, input_ip)
#     if (match):
#         field = input_ip.split(".")
#         for i in range(0, len(field)):
#             if (int(field[i]) < 256):
#                 flag += 1
#             else:
#                 flag = 0
#     if (flag == 4):
#         print("valid ip")
#     else:
#     print('No match for ip or not a valid ip')

import re
def GetIpAddress():
    valid = False
    while not valid:
        ipadd = input("Enter ip address: ")
        IPV4 = re.fullmatch('([0-2][0-5]{2}|\d{2}|\d).([0-2][0-5]{2}|\d{2}|\d).([0-2][0-5]{2}|\d{2}|\d).([0-2][0-5]{2}|\d{2}|\d)', ipadd)
    
        if IPV4:
            valid = True
        
        else:
            print("Invalid IP address. Try again")
    print ("Valid IP address:", ipadd)
GetIpAddress()