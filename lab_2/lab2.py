import string
from collection import counter

#Q1
def word_count(text):
    
    text=text.lower()

    for ch in string.punctuation:
        text=text.replace(ch,"")
    
    words=text.split()

    count={}
    
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    
    return count

#Q2
def word_count_counter(text):
     
    text=text.lower()

    for ch in string.punctuation:
        text=text.replace(ch,"")


    words=text.split()

    
    return Counter(words)


