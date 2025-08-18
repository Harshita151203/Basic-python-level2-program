#  Count frequency of each character.

user_input = input("Enter: ")
freq = {}

for ch in user_input:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1   

# print output
for key, value in freq.items():
    print(f"{key} : {value}")
  