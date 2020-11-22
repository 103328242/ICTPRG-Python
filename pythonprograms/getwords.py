input_valid = False

while input_valid == False:
    print ('\nPlease enter a sentence.  It must have a minimum of 5 words and a maximum of 10 words:\n')
    text_in = input('> ')


    count = len(text_in.split())

    if count < 5:
        print ('\n[+] Your sentence is too short.  Please try again. [+]')
        continue

    elif count > 10:
        print ('\n[+] Your sentence is too long.  Please try again. [+]')
        continue

    else:
        print('\nThank you.')
        input_valid = True

