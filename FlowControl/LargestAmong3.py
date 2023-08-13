a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("A is the largest")
elif b > a and b > c:
    print("B is the largest")
else:
    print("C is the largest")

############################################

a = int(input("Enter First Number:\n"))
b = int(input("Enter Second Number:\n"))
c = int(input("Enter Third Number:\n"))

print(" Largest Number:",end=" ")

if a >= b:

    if a >= c:
        print(a)  # a>=b and a>=c
    else:
        print(c)  # a>=b and c>a
else:
    if b >= c:
        print(b)  # b>a and b>=c
    else:
        print(c)  # b>a and b<c

#################################################

a = int(input("Enter First Number:\n"))
b = int(input("Enter Second Number:\n"))
c = int(input("Enter Third Number:\n"))

print(" Largest Number:", end=" ")

print(max(a,b,c))   # using lib fun: max()