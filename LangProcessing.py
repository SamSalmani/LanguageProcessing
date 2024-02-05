
import matplotlib.pyplot as plt
import os
from collections import Counter

"""counting words in the book
challenges : 1- counting punctuations with the word and need to remove ponctuations
             2- make all texts in lower case"""

def count_words(text):
    
    """ Count the number of times each word occurs in text (str). Retunrs a dictionary
    where keys are unique words and values are word counts. Skip punctuations"""
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch,"")
        
    word_count = {} #using a dictionalry is good for this task
    for word in text. split(" "):
        if word in word_count:  #if the word is known and we had it before
            word_count[word] += 1
        else:                      #if the word is unknown
            word_count[word] = 1
    return word_count


# using Counter function in python to do the task above
def count_words_fast(text):
    
    """ Count the number of times each word occurs in text (str). Retunrs a dictionary
    where keys are unique words and values are word counts. Skip punctuations"""
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = Counter(text.split(" "))
    return word_counts

text = "test text sample"
count_words_fast(text) == count_words_fast(text)  
# They are identical so the type of Counter output is a dictionary


## READING A BOOK
def read_book(title_path):
    """ 
    Read a book and return it as  a string
    """
    with open(title_path, "r", encoding = "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

text = read_book(".\Books\English\shakespeare\Romeo and Juliet.txt")
len(text)
ind = text.find("What's in a name?")

sample_text = text[ind :ind+1000]


## Read, count number of unique words and how many times they are repeated
def word_stats(word_counts):
    
    """ Return number of uniques words and word frequencies"""
    
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

text = read_book(".\Books\English\shakespeare\Romeo and Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts)) #total number of words

# compare Romeo and Juliet in Eng and German
text = read_book(".\Books_GerPort\German\shakespeare\Romeo und Julia.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts)) #total number of words



## Work directories-read all the books in all dirs
book_dir = "./Books"

import pandas as pd
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique")) #create an empty dataframe with 5 cols
title_num = 1 # to add data to the table above, need to tack of the number of the rows. we start from 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir+"/"+language): # including all authors by concatenating path
        for title in os.listdir(book_dir+"/"+language+ "/"+author): #including all titles
            inputfile = book_dir+"/"+language+ "/"+author + "/" + title
            print(inputfile)
            text =  read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
            title_num += 1

stats.head() # check top 5 lines
stats.tail() # check bottom 5 lines
stats.length  #extract each column

plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo")

plt.figure(figsize = (10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of Unique Words")
plt.savefig("lang_plot.pdf")




 


















