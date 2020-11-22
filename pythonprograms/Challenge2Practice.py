import datetime
# import os, sys

output = []
try:
    with open('people.txt') as reader:
        line = reader.readline()
        while line:
            fields = line.strip().split('|')
            f_name = fields[0].lower()
            l_name = fields[1].lower()
            age = int(fields[2])
            if (age < 50) and (f_name[0]!='b'):
                email = f_name[0] + l_name + '@DodnGy.net'
                year = datetime.date.today().year
                birth_year = year - age
                password = '!' + str(birth_year) + l_name.title() + f_name[0].upper() + '_'
                output.append(email + '|' + password)
            line = reader.readline()
except Exception as e:
    print('Exception: ' + str(e))
# try:
#     os.remove('outpass.txt')
# except:
#     pass
with open('outpass.txt','w') as outfile:
    for line in output:
        outfile.write(line + '\n')
print('Done!')


