sentence1 = input("Please insert first sentence ")
sentence2 = input("Please insert second sentence ")
sentence3 = input("Please insert third sentence ")
all_sentences = sentence1 + sentence2 + sentence3
all_sentences.replace(" ", "")

char_amount = {}

for char in all_sentences:
    if char not in char_amount:
        char_amount[char] = 1
    else:
        char_amount[char] += 1

print(char_amount)
