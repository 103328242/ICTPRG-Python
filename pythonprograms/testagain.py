while True:
    menu = int(input('''
    Hello, please select from the following options:
    1. add new order
    2. list orders
    3. exit 
    '''))

    if menu == 1:
        name = input('What is your name?')
        burger = input('How many burgers?')
        fries = input('How many fries?')
        coke = input('How many cokes?')

    if menu == 2:
        print('hello')