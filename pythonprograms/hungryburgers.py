outfile = open("oders.txt","w")
outfile.write("Name|# burgers|# fries|# coke")
outfile.close()

with open('orders.txt','a') as order:
    lines = order.readline()
    print("Menu")
    print ("""
    1.Add new orders
    2.List orders
    3.Exit
    """)
    choice = int(input("Enter your selection: "))
    if choice == 1:
        name = input("Enter your name: ")
        # order.write(name)
        burger = int(input("Enter the no of burgers you need: "))
        fries = int(input("Enter the no of fries you need: "))
        coke = int(input("Enter the no of cokes you need: "))
        # order.write(name|burger|fries|coke)

