# check a number divisible by 2 & 3
num=int(input("Enter your number:"))
if num%2==0:
    if num%3==0:
        print("Divisible by 2 & 3")
    else:
        print("Divible by 2 not by 3")
elif num%3==0:
    print("Divisible by 3")
else:
    print("Neither divisible by 2 nor 3")