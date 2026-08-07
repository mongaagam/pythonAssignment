import string
from collections import Counter

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

#Q3 using loop
def flatten(list_of_list):
    
    result=[]

    for sublist in list_of_list:
        for i in sublist:
            result.append(i)
 

    return result

#using list Comprehension
def flatten_comp(list_of_list):
    
    return [i for sublist in list_of_list for i in sublist]

