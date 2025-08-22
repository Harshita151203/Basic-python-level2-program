# Find Longest Word in a String..


my_str = "Hello, I am ABC"

new = my_str.split()
longest = ""

for ch in new:
    if len(ch) > len(longest):
        longest = ch
print(longest)

