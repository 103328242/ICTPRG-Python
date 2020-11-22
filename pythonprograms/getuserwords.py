min, max = 5, 10
list_words = []
valid = False
while valid is not True:
    list_words.extend(input("Enter between "+ str(min) +" and "+ str(max) +" words:\n").split())
    getwords = input("Enter between "+ str(min) +" and "+ str(max) +" words:\n").lower()
    list_words = getwords.split()
    # if len(list_words) >= min:
    if min <= len(list_words) <= max:
        valid = True
    # #added for testing the max limit
    elif len(list_words) < min:
        print("The sentence you entered needs ", int(min - len(list_words))," to meet the requirement!!")
        # list_words.extend(input("Enter more words: "))
    else:
        print("The words you entered are over the limit of requirement!") 
    
print("Great! Your words are: ")
print(list_words[:10])