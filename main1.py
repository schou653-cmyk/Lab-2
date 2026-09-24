#What's up cool guy -saki

stopwords = set()

with open("stopwords.txt", "r") as file:

    for line in file:
        word = line.strip()
        stopwords.add(word)


textA = []

with open("textA.txt", "r") as file:

    for line in file:
        words = line.lower().split()

        for word in words:
            word = word.strip(".,!?'")
            if word not in stopwords:
                textA.append(word)



textB = []

with open("textB.txt","r") as file:
    for line in file:
        words = line.lower().split()

        for word in words:
            word =  word.strip(",.!?'")
            if word not in stopwords:
                textB.append(word)


textA_counts = {}

for word in textA:
    if word in textA_counts:
        textA_counts[word] += 1
    else:
        textA_counts[word] = 1



for word in textA_counts:
    textA_counts[word] = textA_counts[word] / len(textA)



textB_counts = {}

for word in textB:
    if word in textB_counts:
        textB_counts[word] += 1
    else:
        textB_counts[word] = 1


for word in textB_counts:
    textB_counts[word] = textB_counts[word]/ len(textB)





# This is the main program
# write your program here