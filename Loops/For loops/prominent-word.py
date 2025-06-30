inp = input("Enter a sentence here, and the longest word will be found... ")
inp = inp.split()
wordlen = 0
word = ""
for i in inp:
    length = len(i)
    if length >= wordlen:
        wordlen = length
        word = i
print("The largest word is:",word)
