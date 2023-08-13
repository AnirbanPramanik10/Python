n = int(input("Enter the number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif n < 0:
    if n % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")