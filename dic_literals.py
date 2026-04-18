freq = {}

data = ["apple","banana","apple","orange","apple","banana"]

for item in data:
    if item in freq:
        freq[item]  += 1
        print(item)
        print(freq[item])
    else:
        freq[item] = 1
        print(item)
        print(freq[item])
print(freq)


