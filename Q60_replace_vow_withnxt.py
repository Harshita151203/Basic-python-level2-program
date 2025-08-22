# Replace each vowel with next vowel (a→e, e→i...)

my_txt = input("Enter: ")
vow = "aeiou"
mapping = {"a":"e","e":"i","i":"o","o":"u","u":"a",
           "A":"E","E":"I","I":"O","O":"U","U":"A"}

new = ""

for ch in my_txt:
    if ch in mapping:
        new += mapping[ch]
    else:
        new += ch
print("New String:",new)