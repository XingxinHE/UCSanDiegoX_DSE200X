import collections

#open the file
file = open("98-0.txt", encoding = "utf8")

#explict the common words like "the"
stopwords = set(line.strip() for line in open('stopwords'))

#create the dictionary
wordCounts = {}

#1.read the file, lower case, and split them 
#2.transfer all the punctuation to nothing
#3.filter, if they are not in stopwords, then run below
#4.manage the dict
for word in file.read().lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("\"", "")
    word = word.replace("“","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
        
#count the word, use the library collections
d = collections.Counter(wordCounts)

for word, count in d.most_common(10):
    print("The word '"+word+"' shows "+str(count)+" times in this novel.")
    
