# import re

# def GetEmailAddress(email):
#     # email = input("Enter email address: ")
#     if len(email) > 7:
#         return bool(re.match("^,+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0,9]{1,3}(]?)$", email))
# GetEmailAddress("basil.joseph@gmail.com")
def HasValidLength(input):
    return len(input) >= 2 and len(input) <= 32 

def IsValidEmail(email):
    try:
        AtList = email.split("@")
        DoList = AtList[1].split('.')
        return len(DoList) < 2 and not(HasValidLength(AtList[0])) and HasValidLength(DoList[0])
    except:
        return False

emailInput = "Invalid"

while(not(IsValidEmail(emailInput))):
    emailInput = input("Please enter a valid email: ")

print(emailInput)
