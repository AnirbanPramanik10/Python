s = {10, 20, 30}
print(s)

s1 = set([10, 20, 30])
print(s1)

s2 = {}
print(type(s2))

s3 = set()
print(s3)

s.add(40)
print(s)

s.add(50)
print(s)

s.update({60, 70})
print(s)

s.update({90}, {100})
print(s)



################################

# Removal functions

s = {10, 20, 30, 40}
s.discard(30)
print(s)

s.remove(20)
print(s)

s.clear()
print(s)

del s
########################


s1 = {10, 20, 30}
s2 = {20, 40, 50}
# print('union ', s1 | s2)
print(s1.union(s2))

# print('intersecton', s1 & s2)
print(s1.intersection(s2))

# print('present in s1, but not present in s2', s1 - s2)
print(s1.difference(s2))

print('symmetric differences, not present in both', s1 ^ s2)


