d = {}
while True:
    print("1.add a word to the dictionary")
    print("2.view the words in the dictionary")
    print("3.delete a word from the dictionary")
    print("4.retreive a word from the dictionary")
    print("5.exit")
    choice = int(input("what would you like to do"))
    if choice == 1:
        key =  input("what word would you like to add to the dictionary")
        storage = input("please give a desciption of the word")
        d[key] = storage
    if choice == 2:
        print (d)
    if choice == 3: 
        gloss = (input("what word would you like to delete"))
        del d[gloss]    
    if choice == 4:
        m = input("what word would you like a description")
        print(d[m])
    if choice ==5:
        break