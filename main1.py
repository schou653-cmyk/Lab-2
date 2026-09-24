#What's up cool guy -saki

stopwords = set()

with open("stopwords.txt", "r") as file:

    for line in file:
        word = line.strip()
        stopwords.add(word)


textA = []

with open("textA.txt", "r") as file:

    for linee in file:
        words = line.split()

        for word in words:
            if word not in stopwords:
                textA.append(word)

print(textA)








# This is the main program
# write your program here