# word reversal

word=input("enter the word")
new_word=""
for i in reversed(word):
    new_word+=i
print(new_word)