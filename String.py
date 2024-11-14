
words = []
amount = []


for i in range(10):
    wordinput = input("Enter word: ")
    words.append(wordinput)

lengthinput = int(input("Enter a lenght/number: "))
for words in words:
    if len(words) == lengthinput:
        amount.append(words)
    else:
        continue
print(amount)
