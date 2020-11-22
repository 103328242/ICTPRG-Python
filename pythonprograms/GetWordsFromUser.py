
word_list = []
valid = False
while not valid:
    min = 5
    max = 10
    getwords = input("Please enter a sentence with a minimum of 10 words and a maximum of 20 words: ")
    words = getwords.lower().split()
    word_count = len(words)
   
    if word_count < min:
        print("The word count is short. Please try again: ")
        continue
    elif word_count > max:
        print("The word count is long. Please try again: ")
        continue
    else:
        valid = True
        print("\nYour sentence is: '",str(getwords) ,"'""\n\nThere are '",word_count,"' words in your sentance!!"" \n\nAnd the words are: ", words,"\n")
     
        
#     elif x < min:
#         print("Word count not met. Enter", int(min-x)," more words!!")
#         # word_list.append(getwords)

#     else:
#         print("The word count is over the countlimit.")
# print("The words you entered are: ")
# print(word_list)
# print(words)





# test_string = "Geeksforgeeks is best Computer Science Portal"
  
# # printing original string 
# print ("The original string is : " +  test_string) 
  
# # using split() 
# # to count words in string 
# res = len(test_string.split()) 
  
# printing result 
# print ("The number of words in string are : " +  str(res)) 