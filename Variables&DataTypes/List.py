arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[4])
print(arr[-1])
print(arr[-5])


########################

# Insert & Search Operations

arr.append(30)
print(arr)

arr.insert(2, 20)
print(arr)

print(20 in arr)

print(arr.__contains__(15))

print(arr.count(20))

print(arr.index(40))


############################

l = [10, 20, 30, 40, 50, 60, 70, 80, 90]

l.remove(20)
print(l)

print(l.pop())
print(l)

print(l.pop(2))
print(l)

del l[1]
print(l)

del l[0: 2]
print(l)


##########################

# Some more general functions

a = [10, 20, 30, 40, 50]

print(max(a))
print(min(a))
print(sum(a))

a.reverse()
print(a)

a.sort()
print(a)