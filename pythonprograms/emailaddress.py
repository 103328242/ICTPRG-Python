import re

def GetEmailAddress(pattern):
    return re.match(r"[\w+.-_]{2,32}@\w{2,32}\.[\w.]{2,3}$", pattern)
    # return re.match(r"^[\w\.\+\-]{2,32}@[\w]{2,32}.[a-z]{2,3}$", pattern)

valid = False

while not valid:
    email_input = input("Enter your email >>")
    validate = GetEmailAddress(email_input)
    # validate = GetEmailAddress(input("Enter your email >>"))

    if validate:
        print("Your email '"+email_input+"' is Valid.")
        # print("valid")
        valid = True
    else:
        print("Your email '"+email_input+"' is invalid!. Please enter a valid email!")
        # print("Invalid")
        # continue
        


