print("Would you like to reverse the words, sentence, or both?")
selector = input("Please type your selection: ")
selector = selector.lower() # Converts all inputs to lowercase

if selector == "sentence":
    sentence = input("Please input your sentence: ")
    split_sen = sentence.split(" ")
    rev_sen = []
    for words in split_sen:
        rev_sen.insert(0,words)
    print(" ".join(rev_sen))

elif selector == "words":
    sentence = input("Please input your sentence: ")
    split_sen = sentence.split(" ")
    rev_words = []
    for words in split_sen:
        words = words [::-1]
        rev_words.append(words)
    print(" ".join(rev_words))

elif selector == "both":
    sentence = input("Please input your sentence: ")
    print(sentence[::-1])

else: 
    print("Your selection does not match any of the options!")
print("Thankyou for using this program!")



