# Count how many words are of length >= 5.

my_sent = input("Enter Your Sentence: ")
a = my_sent.split()

count = 0


for ch in a:
    if len(ch) >= 5:
        count += 1
print(count)