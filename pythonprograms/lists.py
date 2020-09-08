#Lists (Arrays)
#Multiple values stored in single variable

#sentence = "Test Sentence"

#Index:  0 1 2 3  4 5 6 7 8 9 10 11 
#Value:  T e s t  S e n t e n  c  e   

#https://www.programiz.com/python-programming/list


#values = [66, 43, 1, 6, 2, 99, 4]

#for x in values:
#    if x < 10:
#        print(x)

#userdate = str(input("Today's date in dd/mm/yyyy format: "))
#print("Todays date is: "+ userdate)
#date = userdate.split('/')
#print("Date: "+ date[0])
#print("Month: "+ date[1])
#print("Year: "+ date[2])

#values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
#Sum = sum(values)
#print("Sum is: "+ str(Sum))
#count = len(values)
#Avg = Sum / count
#print("Avg is: "+ str(Avg))
#Max = max(values)
#print("Max value in the list is: "+ str(Max))

#Write a program that enters a string containing a person's full name and then output their initials
#Name = input("Enter your full name: ")
#name = ''
#for i,j in enumerate(Name):
#    if i == 0:
#        name+=(j+'')
#    elif j == ' ':
#        name += (Name[i+1]+'')
#print(name)
  



#name = input("Please enter a name: ")
#names = name.split()
#initials = [x[0] for x in names[:-1]]
#print(*initials, names[-1])

#user = input('Please Enter your name \n')
#names = user.split()

#for i in range(0, len(names)):
#    if i < len(names) - 1:
#        # print first char only, no newline at the end
#        #print(names[i][0], end=" ") 
#        print(names[i][0])


#intitials = ""
#name = input("Enter your full name: ")
#print(name)
#Name = name.split()
#print(Name)
#for x in Name:
#    intitials += x[0]
#print(intitials.upper())



#initial = []
#while True:
#    nums = input("Enter numbers: ")
#    if nums != 'x':
#        initial.append(int(nums))      
#    else:
#        break
#print("You Entered: ", initial)
# 
#    
#output = ''
#total = 0
#num = input('Enter a large number: ')
#count = 1
#length = len(num)
#for x in num:
#    output += x
#    total += int(x)
#    if (count != length):
#        output += '+'
#    count += 1
#print("Sum of all digits is: ", output + ' = ' + str(total))

#    if (x == num and total = 0 and num[0] != 0)
 #       large += '+'
  #  large += x
#
#list_num =[]
#i=0

#for i in large_num:
#    list_num.append(int(i))

#print(sum(list_num))

numbers = []
repeaters = []
while True:
    number = input("Please enter number: ")
    if number == 'x':
        break
    else:
        if numbers.count(int(number)) > 0:
            if repeaters.count(int(number)) == 0:
                repeaters.append(int(number))
        else:
            numbers.append(int(number))
repeaters.sort()
print(repeaters)


























