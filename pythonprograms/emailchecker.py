import re
def email():
    email = input("enter the mail address::")
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)

    if match:
        print ("valid email :::", match.group())
    else:
        print ("not valid:::")

email()