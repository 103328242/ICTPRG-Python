#square
print("Number\tSquare")
print("--------------")
for x in range(8):
	# x as each of 0,1,2,3,4,5,6,7 exit
    print(str(x+1) + "\t" + str((x+1) * (x+1)))

#another way same result
print("Number\tSquare")
print("--------------")
for x in range(1,9):
    print(str(x) + "\t" + str(x * x))

#another example

for x in "banana":
    print(x)

#Excercise1
for  y in [0,1,2,3,4,5,6,7,8,9]:
    print("I love programming")

#2
for x in range (5):
    print(x)

#3
for count in range (1,5,-2):
    print(count)
#4
salary = int(input("Enter your salary: "))
time = int(input("Enter years of work: "))

if salary >= 5000 and time >= 3:
    print("Loan Approved!")
else:
    if salary < 5000 and time >= 3:
        print("salary low, rejected!")
    else:
        if salary>=5000 and time <3:
            print("Time is not enough, Rejected!")
        else: 
            print("Neither criteira met. Rejected!")

