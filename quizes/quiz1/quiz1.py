def get_word(sentence, n):
    if n>0:
        words=sentence.split(" ")
        # print(words)
    
        if n<=len(words):
            return words[n-1]
    # return("words") 

print(get_word("This is a lesson about lists", 4))
print(get_word("This is a lesson",-4))
print(get_word("Now we are cooking!", 1))
print(get_word("Now we are cooking!", 5))