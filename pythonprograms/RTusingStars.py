#Write a method that can print a right angle triangle using only 1 (one) of both print('x', end='') and print("").
num = int(input("Enter the number of rows: ")) #Taking the user input for numberof Rows.
for i in range(1,num+1):    #This checks the Row;num+1 coz the second part is excluded in range(), ie. for 1-10: range(1,11)
    for j in range(1,i+1):  #This checks the column.
        print("*",end=" ")  #Prints the * and ends after space
    print()                 #Provides new line,ie new row  