text = input("Enter a sentence: ")
sentence = {}
words = text.split()
for word in words:
    sentence[word] = sentence.get(word, 0) +1
words = list(sentence.keys())
words.sort()
for word in words:
    print("{:5} : {}".format(word, sentence[word]))