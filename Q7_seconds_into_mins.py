# Input seconds and convert to minutes and seconds.

# 1 min = 60sec

num = int(input("Enter:"))
min = num//60
sec = num % 60       

print(f"{min:02}:{sec:02}")


