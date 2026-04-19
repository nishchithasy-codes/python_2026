file = open("sample.txt","r")
text = file.read().lower()
words = text.split()

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
sorted_words = sorted(freq.items(),key = lambda x:x[1],reverse = True)

print("Top 10 frequent words are: ")

for i in range(min(10,len(sorted_words))):
    print(sorted_words[i])
    