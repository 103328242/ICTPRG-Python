#count = 10
#count1 = 11
#while count1 <= 50:
#    print(count)
#    count += count1
#    count1 += 1
    
#num = int(input("Enter a number: "))
#while num!=0:
#    if num > 50 and num < 70:
#        print("Congrats!! The number is Within Range.")
#        break
#    else:
#        print ("Sorry. Not in Range.")
#        num = int(input("Try again: "))
#for x in range(0,26):
#    print(x, sep=',')

#print(*range(0,26), sep=',')

#num = int(input("Enter the number of rows: "))
#for i in range(5):
#    for j in range(5):
#        print("x", end='')
#    print()
#for i in range(1,7):
#    for i in range(1,10):
#       print("x", end=" ")
#   print()

#count = 0
#while count < 26:
#    print(count)
#    count += 1
#count = 10
#count1 = 11
#while count1 <= 50:
#    print(count)
#    count += count1
#    count1 += 1
#num = int(input("Enter a number: "))
#while num!=0:
#    if num > 50 and num < 70:
#        print("Congrats!! The number is Within Range.")
#        break
#    else:
#        print ("Sorry. Not in Range.")
#        num = int(input("Try again: "))

#print(*range(0,26), sep=',')

total=0
while True:
    num = input("Enter some numbers (Press x to stop):\n")
    if num != "x":
        total += int(num)
    else:
        print("Total: ", total)
        break


