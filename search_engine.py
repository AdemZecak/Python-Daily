search = "how to create a password generator using python"

words = search.split()

counts = {}
count = 0 

for i in range(0,len(words)):
    firstword = words[i]
    for i in range(0,len(words)):
        secondword = words[i]
        if firstword == secondword:
            count += 1
    counts[firstword] = count
    count = 0 


print(counts) 