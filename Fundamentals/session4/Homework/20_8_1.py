from string import ascii_letters
count = {}
letters = list(ascii_letters)

sentence = input("Enter your sentence: ")
convert_sentence = str.lower(sentence)

for word1 in letters:
    for word2 in convert_sentence:
        if word1 == word2:
            count[word1] = count.get(word1, 0) + 1

for k, v in count.items():
    print(k, v)
