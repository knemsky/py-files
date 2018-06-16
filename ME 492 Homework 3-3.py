#Kurtis Nemsky

Vowels = ['a','e','i','o','u']

word = str(input("Please enter a word that should be changed: "))
x = word[0]
y = word[1:]
if x in Vowels:
    new_word = str(word+'hay')
else:
    new_word = str(y+x+'ay')
print(new_word)
