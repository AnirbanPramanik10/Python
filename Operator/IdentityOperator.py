x = 10

y = x

print("x and y has same address:", x is y)

print(x is not y)

###################################################

x1 = 10
x2 = 10

y1 = 10.5
y2 = 10.5

z1 = "geeksforgeeks"
z2 = "geeksforgeeks"

print("x1 is x2:",x1 is x2)     # python allocate same memory for same literal

print("y1 is y2:",y1 is y2)

print("z1 is z2", z1 is z2)



#######################################################

l1 = [10, 20, 30]

l2 = [10, 20, 30]

print("li is l2:", l1 is l2) # value is same but is give false. but in string and int it gives true
