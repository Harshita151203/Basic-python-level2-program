#Input a number as string, convert to int and multiply by 10.

try:
    user_choice = input("Enter: ")
    print(type(user_choice))
    new_num = int(user_choice)
    print(type(new_num))
    print(new_num*10)
except ValueError:
    print("Please Enter a Valid Input")