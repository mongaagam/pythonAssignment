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
   
#using List Comprehension
def flatten_comp(list_of_list):
    
    return [item for sublist in list_of_list for item in sublist]



#Q4
def mean_of_file(path):
      
    total=0
    count=0
    
    with open(path,"r") as file:
        
        for line in file: 
            
            try: 
                num=float(line)
                total+=num
                count+=1
            
            except ValueError: 
                pass
      
    if count==0:
        return 0

    return total/count 

#Q5
#List comrehension creates the complete list in memory
#Generate expression cerates one value at a time and use less memory


#Q6
if __name__ == "__main__":

    print("Q1:")
    print(word_count("Hello, hello World!"))

    print("\nQ2:")
    print(word_count_counter("Hello, hello World-"))

    print("\nQ3 (Using Loop):")
    print(flatten([[1, 2], [3, 4], [5]]))

    print("\nQ3 (Using List Comprehension):")
    print(flatten_comp([[1, 2], [3, 4], [5]]))

    print("\nQ4:")

    try:
        print(mean_of_file("number.txt"))

    except FileNotFoundError:
        print("File not found")
