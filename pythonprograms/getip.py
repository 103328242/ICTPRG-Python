# s = input("Enter an IP address: ")
# def validate_ip(s):
#     a = s.split('.')
#     if len(a) != 4:
#         return False
#     for x in a:
#         if not x.isdigit():
#             return False
#         i = int(x)
#         if i < 0 or i > 255:
#             return False
#     return True

# import ipaddress
# #ipadd = input("Enter ip address: ")
# def GetIpAddress(string):
#     try:#         ipaddress.IPv4Network(string)
#         return True
#     except ValueError:
#         return False

# import socket
# #addr = '127.0.0.2561'
# addr = input("Enter an IP address: ")
# try:
#     socket.inet_aton(addr)
#     print(addr+" is Valid IP")

# except socket.error:
#     print(addr+" is Invalid IP")

#import re
#ipRange = '^(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))\.(\d|[1-9]\d|1\d\d|2([0-4]\d|5[0-5]))$'
# ipRange = "^(([1-9]?\d|1\d\d|25[0-5]|2[0-4]\d)\.){3}([1-9]?\d|1\d\d|25[0-5]|2[0-4]\d)$"
# def GetIpAddress(ipaddr):
#     try:
#         if(re.search(ipRange,ipaddr)):
#             print(ipaddr," is Valid Ip address")
#         else:
#             print(ipaddr," is Invalid Ip address")
#     except Exception as e:
#         print(e)



# ipaddr = "192.168.1.1"
# GetIpAddress(ipaddr)
# ipaddr = "333.2.1.1"
# GetIpAddress(ipaddr)
# ipaddr = "wwjcjvdcjgd"
# GetIpAddress(ipaddr)
# import socket
# ip4 = input("Enter an Ip address: ")
# def GetIpAddress(ip4):
#     try:
#         x = socket.inet_pton(socket.AF_INET, ip4)
#         print(x)
#         print("Valid ip4\n")
#     except AttributeError:  # no inet_pton here, sorry
#         print("no inet_pton here, sorry\n")
#         try:
#             y = socket.inet_aton(ip4)
#             print(y)
#         except socket.error:
#             print("error, inet_aton\n")
#             return False
#         return ip4.count('.') == 3
#     except socket.error:  # not a valid address
#         print("not a valid ip4 address\n")
#         return False

#     return True

# def is_valid_ipv6_address(ip6):
#     try:
#         w = socket.inet_pton(socket.AF_INET6, ip6)
#         print(w)
#         print("Valid ip6\n")
#     except socket.error:  # not a valid address
#         print(" not a valid ip6 address\n")
#         return False
#     return True

# address = "192.168.1.1"
# GetIpAddress(ip4)
# address = "2001::20AF"
# is_valid_ipv6_address(ip6)
# address = "300.55.66.22"
# GetIpAddress(ip4)
# address = "192.168.1.1.2"
# GetIpAddress(ip4)
# address = "200:6555::02001"
# is_valid_ipv6_address(ip6)`
# 
s = input("Enter and IP address: ")
def isgoodipv4(s):
    while True:
        #s = input("Enter and IP address: ")
        pieces = s.split('.')
        if len(pieces) != 4: 
            print("Not valid ip4!!!!\n")
            return False
        try:
            print("valid ip4!!!\n")
            return all(0<=int(p)<256 for p in pieces)
            

        except ValueError: 
            print("Error!!")
            return False

