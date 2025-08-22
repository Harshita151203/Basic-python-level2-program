# replace digit with X.

num = input("Enter: ")
new = ""
for ch in num:
    if ch.isdigit():
      new += "X"
    else:
       new += ch
print(new)
    



