# outfile = open("orders.txt","a")
# outfile.write("Name|# burgers|# fries|# coke\n")
# outfile.close()
# with open('orders.txt','a') as order:
    #lines = order.readline()
orders = []
while True:    
    print("Menu")
    print ("""
    1.Add new orders
    2.List orders
    3.Exit
    """)
    choice = int(input("Enter you choice: "))
    if choice == 1:
        with open('orders.txt', 'a') as order:
            name = input("Enter your name: ")
            order.write(name +'|')
            burger = input("Enter the no of burgers you need: ")
            order.write(burger +'|')
            fries = input("Enter the no of fries you need: ")
            order.write(fries +'|')
            coke = input("Enter the no of cokes you need: ")
            order.write(coke +'')
            print("Thank you for your order. Your order is on it way.")
            orders.append([name,burger,fries,coke])
            order.write(f'{name}|{burger}|{fries}|{coke}\n')

    elif choice == 2:
        if len(orders) == 0:
            print("No orders placed!\n")
        else:
            counter = 1
            for o in orders:
                print(str(counter) +'. '+o[0]+', '+o[1]+' burgers'+', '+o[2]+' fries'+', '+o[3]+' cokes')
                counter += 1
            
        # with open('orders.txt') as line:
        #     # a,b,c,d = line.strip().split('|')
        #     a,b,c,d = line.split('|')
        #     read_orders = (f'{a},\t\t{b} Burger(s), {c} Fries, {d} Cokes')
        #     print(read_orders)
        # # lines = display.readlines()
            # lines = display.read()
            # disp_list = lines.split('|')
            # print(disp_list)
            # break
        # for line in lines:
        #     print(line)
    elif choice == 3:   
        print("Thank you for coming.. Bye!")
        break
    else:
        print("Invalid Entry.")
print("Thanks for waiting. Please collect your order.")

