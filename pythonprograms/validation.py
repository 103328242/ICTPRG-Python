# while(True):
#    #take input as string
#    name = input('Enter age : ')
#    #check if valid age, only digits
#    print( name.isdigit() ) 
#    break

while True:
   num = input("Enter number: ")
   if num.isdigit():
      break
   else:
      print("not valid try again.")
print("Valid " +num)