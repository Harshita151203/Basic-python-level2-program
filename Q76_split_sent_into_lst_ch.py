# split sentence into list of characters.

mysent = input("Enter Your Sentence: ")
new = []

for ch in mysent:
    if ch != " ":
        new.append(ch)
    
print(new)