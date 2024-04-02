import os
import string

filepath = ("C:/Users\Danbo\Documents/UoN_CompSci\Year 3\COMP3003\Project/NLGlite\src\data/text/books/scarlet.txt")
data = ""

if os.path.exists(filepath):
    if filepath.endswith(".txt"):
        f = open(filepath, "r", encoding="utf-8", errors="ignore")
        # add each line to the data string
        for line in f:
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.lower()
            line = line.replace("\n", "")
            data += line + " "
        f.close()

frequency = {}
for word in data.split(" "):
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_by_value = sorted(frequency.items(), key=lambda item: item[1])
# Optional: convert back to dictionary
sorted_dict = dict(sorted_by_value)

total = 0
for item in sorted_dict:
    total = total + sorted_dict.get(item)

print(len(sorted_dict))

print(total / len(sorted_dict))
