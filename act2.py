def match_words(words):
    ctr=0
    lst = []
    
    for word in words:
        if len (word) > (1) and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
            
    print("list of words that are same from first charecter and last character same \n")
    return ctr
count=match_words(["abc","ece","dfg","ihi" "1221"])
print("number of words having first and last character same",count)
    
    