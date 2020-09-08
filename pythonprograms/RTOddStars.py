#Odd number pattern
num = int(input("Enter the number of rows: ")) #Taking the user input for numberof Rows.
k=1
for i in range(1,num+1):    #This checks the Row;num+1 coz the second part is excluded in range(), ie. for 1-10: range(1,11)
    for j in range(1,k+1):  #This checks the column.
        print("*",end=" ")  #Prints the * and ends after space
    k=k+2                   #Increments the value of k
    print()                 #Provides new line,ie new row  