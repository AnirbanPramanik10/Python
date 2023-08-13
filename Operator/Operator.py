x = input("Enter the 1st no:")
y = input("Enter the second no:")

# Arithmetic #

x = int(x)
y = int(y)

print("addition:", x + y)

print("subtraction:", x - y)

print("multiplication:", x * y)

print("float division:", x / y)

print("integer division:", x // y)

print("remainder:", x % y)

print("power:", x ** y)


###############################################

# Logical #

a = 10
b = 20
c = 30

print('and:- both should be true: a<b and b<c:', a < b and b < c)

print('or: a<b or b>c:', a < b or b > c)

print('not: a>b:',not a > b)

# ---------------------------------- #
s1 = ''

s2 = s1 or 'defaultStr'

print(" in case of false, default value taken s2:", s2)

l1 = []

l2 = l1 or [1, 2, 3]

print(" in case of true, default value taken l2:", l2)

# --------------------------------------- #

x = 10

print(" x or 30: ", x or 30)  # in "or" if 1st value is true, 2nd not considered

y = 0

print("y or 30", y or 30)  #

z = 40

print(" z and 50:", z and 50)  # in "and" value till last is considered,
