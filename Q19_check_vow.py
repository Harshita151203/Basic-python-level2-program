#  Check if entered char is vowel using membership test.

my_char = input("Enter: ")

for i in my_char:
    if i in "aeiouAEIOU":
        print("YES", i)


