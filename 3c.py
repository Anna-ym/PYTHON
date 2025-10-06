word=input("Enter a word:")
print(word)
vowels=['a','e','i','o','u']
y=len(word)
print(y)
for i in word:
    if i in vowels:
        print(i)