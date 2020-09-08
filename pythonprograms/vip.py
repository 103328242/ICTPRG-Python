#def func(i):
#  for x in range(1, i+1):
      # print ("At the TOP x is %d" %x)
      # numbers.append(x)
#       x=x+1
      # print ("At the bottom x is %d" %x)

 #  print ("The numbers:")
  # for i in numbers:
  #     print (i)

#i = int(input("Enter the number: "))
#print ("I'm going to print the numbers!")
#func(i)
# Python program to print all the numbers within an interval 
#l = 1
#num = int(input("Enter the number: "))
#for num in range(l, num + 1): 
#    print(num) 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is", +largest)