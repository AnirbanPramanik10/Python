print(id(5))
a = 20
print(id(a))
b = a
print(id(b))

###########################

x = 10
y = 10
print(id(x))  # In python Literals are stored in same locations if they have same value and x & y are just references
print(id(y))


##############################


# Is --- uses gives boolean valur True or False

x = 10
y = 10
print(x is y)

a = "Leo"
b = "Messi"
print(a is b)